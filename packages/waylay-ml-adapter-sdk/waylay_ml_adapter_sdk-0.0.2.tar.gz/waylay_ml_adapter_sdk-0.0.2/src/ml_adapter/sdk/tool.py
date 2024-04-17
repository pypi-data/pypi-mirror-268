"""Service tool for the ml-adapters."""

import contextlib
import logging
from collections import namedtuple
from collections.abc import AsyncIterator
from functools import cached_property
from types import SimpleNamespace
from typing import Optional, TypeVar, Union, cast

from ml_adapter.api.data.common import V1_PROTOCOL
from ml_adapter.base.assets.manifest import ManifestSpec, WithManifest
from pydantic import TypeAdapter
from tenacity import retry, stop_after_delay, wait_exponential
from waylay.sdk import WaylayTool
from waylay.sdk.exceptions import WaylayError
from waylay.services.registry.api import PlugsApi, WebscriptsApi
from waylay.services.registry.models import (
    EventWithCloseSSE,
    GetPlugResponseV2,
    GetWebscriptResponseV2,
    PostPlugJobAsyncResponseV2,
    PostPlugJobSyncResponseV2,
    PostWebscriptJobAsyncResponseV2,
    PostWebscriptJobSyncResponseV2,
)
from waylay.services.registry.service.service import RegistryService
from waylay.services.rules.service.service import RulesService

WebscriptResponse = Union[
    PostWebscriptJobAsyncResponseV2,
    PostWebscriptJobSyncResponseV2,
    GetWebscriptResponseV2,
]

T = TypeVar("T")

LOG = logging.getLogger(__name__)

STREAM_TIMEOUTS = (5.0, None, 5.0, 5.0)

FunctionResponse = GetWebscriptResponseV2 | GetPlugResponseV2
JobResponse = (
    PostWebscriptJobAsyncResponseV2 | PostPlugJobAsyncResponseV2 | FunctionResponse
)
CreateResponse = (
    PostWebscriptJobAsyncResponseV2
    | PostWebscriptJobSyncResponseV2
    | PostPlugJobAsyncResponseV2
    | PostPlugJobSyncResponseV2
)

_FunctionRef = namedtuple("FunctionRef", ["name", "version"])


class MLTool(WaylayTool):
    """MLAdapter utility service for the waylay client."""

    name = "ml_tool"
    title: str = "ML Adapter Tool"
    description: Optional[str] = """
Helps creating waylay webscripts and plugs that wrap a machine learning model.
"""

    @cached_property
    def registry(self) -> RegistryService:
        """Get the registry SDK."""
        return self._services.require(RegistryService)

    @cached_property
    def rules(self) -> RulesService:
        """Get the registry SDK."""
        return self._services.require(RulesService)

    @cached_property
    def webscripts(self) -> WebscriptsApi:
        """Get the registry SDK."""
        return self.registry.webscripts

    @cached_property
    def plugs(self) -> PlugsApi:
        """Get the registry SDK."""
        return self.registry.plugs

    async def python_runtimes(self):
        """Check registry version."""
        resp = await self.registry.runtimes.list(
            query={"archive_format": ["python"]}, select_path=""
        )
        return SimpleNamespace(**{r.function_type: r for r in resp.runtimes})

    async def create_webscript(
        self,
        adapter: WithManifest,
        manifest: Optional[ManifestSpec] = None,
        name: Optional[str] = None,
        version: Optional[str] = None,
        runtime: Optional[str] = None,
        comment: str = "",
        draft: bool = False,
        var_async: bool = True,
    ) -> PostWebscriptJobAsyncResponseV2 | PostWebscriptJobSyncResponseV2:
        """Create a webscript function from the given ml adapter."""
        manifest = manifest or {}
        if name:
            manifest = {**manifest, "name": name}
        if version:
            manifest = {**manifest, "version": version}
        if runtime:
            manifest = {**manifest, "runtime": runtime}
        adapter = adapter.as_webscript(manifest)
        await adapter.save()
        with contextlib.ExitStack() as stack:
            # uses ExitStack.enter_context to close files afterwards.
            files = {
                asset.full_path: stack.enter_context(open(asset.location, "br"))
                for asset in adapter.assets.iter(
                    recursive=True,
                    include_dir=False,
                    exclude_empty=True,
                )
            }
            result = await self.webscripts.create(
                files=files,
                query={"draft": draft, "comment": comment, "async": var_async},
                select_path="",
            )
        return result

    async def create_plug(
        self,
        adapter: WithManifest,
        manifest: Optional[ManifestSpec] = None,
        states: Optional[list] = None,
        inputs: Optional[dict] = None,
        outputs: Optional[dict] = None,
        name: Optional[str] = None,
        version: Optional[str] = None,
        runtime: Optional[str] = None,
        comment: str = "",
        draft: bool = False,
        var_async: bool = True,
    ) -> PostPlugJobAsyncResponseV2 | PostPlugJobSyncResponseV2:
        """Create a plug function from the given ml adapter."""
        manifest = manifest or {}
        if name:
            manifest = {**manifest, "name": name}
        if version:
            manifest = {**manifest, "version": version}
        if runtime:
            manifest = {**manifest, "runtime": runtime}
        interface = manifest.get("interface") or {}
        interface_doc = manifest.get("metadata", {}).get("interface", {})
        if states:
            interface["states"] = states
            manifest["interface"] = interface
            del interface_doc["states"]
        if inputs:
            interface["inputs"] = inputs
            manifest["interface"] = interface
            del interface_doc["inputs"]
        if outputs:
            interface["outputs"] = outputs
            manifest["interface"] = interface
            del interface_doc["outputs"]
        adapter = adapter.as_plug(manifest)
        await adapter.save()
        with contextlib.ExitStack() as stack:
            # uses ExitStack.enter_context to close files afterwards.
            files = {
                asset.full_path: stack.enter_context(open(asset.location, "br"))
                for asset in adapter.assets.iter(
                    recursive=True,
                    include_dir=False,
                    exclude_empty=True,
                )
            }
            result = await self.plugs.create(
                files=files,
                query={"draft": draft, "comment": comment, "async": var_async},
                select_path="",
            )
        return result

    async def wait_until_ready(
        self,
        resp: (CreateResponse | dict),
        logger: Optional[logging.Logger] = None,
        success_states=("running",),
    ):
        """Wait for a webscript to be running."""
        create_resp: CreateResponse = _as_model(resp, CreateResponse)
        status = create_resp.entity.status
        is_webscript = hasattr(create_resp.entity, "webscript")
        ref = create_resp.entity.webscript if is_webscript else create_resp.entity.plug
        if status not in success_states:
            jobs_resp: JobResponse
            if isinstance(create_resp, PostPlugJobSyncResponseV2):
                jobs_resp = await self.plugs.get(ref.name, ref.version)
            elif isinstance(create_resp, PostWebscriptJobSyncResponseV2):
                jobs_resp = await self.webscripts.get(ref.name, ref.version)
            else:
                jobs_resp = create_resp
            logger = logger or LOG
            logger.info("Waiting for %s@%s to be ready:", ref.name, ref.version)
            event_href: str
            event_link = getattr(jobs_resp.links, "event", None)
            if not event_link:
                raise WaylayError("no event link available")
            event_href = event_link.href
            logger.info("listening on %s", event_href)
            _last_event = await self.log_events(event_href, logger)

        if is_webscript:
            result = await self.webscripts.get(ref.name, ref.version)
        else:
            result = await self.plugs.get(ref.name, ref.version)
        status = result.entity.status
        logger.info("function %s@%s has status %s", ref.name, ref.version, status)
        if status in success_states:
            return result
        raise WaylayError(f"Deployment failed: {result.entity.failure_reason}")

    def _log_event(
        self, event: EventWithCloseSSE, logger: Optional[logging.Logger] = None
    ):
        logger = logger or LOG
        event_type = getattr(event, "event", None)
        if event_type is None:
            logger.warning("%s", event)
            return event_type
        event_info = getattr(event, "data", None)
        job = getattr(event_info, "job", "")
        job_type = getattr(job, "type", "")
        if job_type == "":
            logger.info("%s\n%s", event_type, event_info)
            return event_type
        func = getattr(event_info, "function", "")
        func_name = getattr(func, "name", "")
        func_version = getattr(func, "version", "")
        func_ref = f"{func_name}@{func_version}" if func else ""
        event_log = f"{func_ref} {job_type}: {event_type}"
        if event_type in ["completed", "failed"]:
            event_log += f"\n{event_info}"
        logger.info("%s", event_log)
        return event_type

    async def log_events(
        self,
        query_or_url: Union[str, dict],
        logger: Optional[logging.Logger] = None,
        close_on_event: tuple[str] = ("close",),
    ):
        """Log job events for the given url or query."""
        iter_events = await self.iter_events(query_or_url)
        async for event in iter_events:
            event_type = self._log_event(event, logger)
            if event_type in close_on_event:
                return event

    async def iter_events(
        self, query_or_url: Union[str, dict]
    ) -> AsyncIterator[EventWithCloseSSE]:
        """Iterate over job events."""
        if isinstance(query_or_url, str):
            iterator = await self.registry.api_client.request(
                "GET",
                query_or_url,
                stream=True,
                timeout=STREAM_TIMEOUTS,
                response_type=EventWithCloseSSE,
            )
            return cast(AsyncIterator[EventWithCloseSSE], iterator)
        else:
            return await self.registry.jobs.events(
                query=query_or_url,
                stream=True,
                timeout=STREAM_TIMEOUTS,
                # TODO ,validate_query=False
            )

    async def test_webscript(self, ref: GetWebscriptResponseV2 | dict, instances):
        """Test invocation of a deployed ml function."""
        func_resp = _as_model(ref, GetWebscriptResponseV2)
        invoke_link = func_resp.links.invoke
        if not invoke_link:
            raise WaylayError("No invocation link available")
        resp = await self.api_client.request(
            "POST", invoke_link.href, json={"instances": instances}, raw_response=True
        )
        data = resp.json()
        data = data.get("predictions", data)
        return data

    async def test_plug(
        self, ref: GetPlugResponseV2 | dict, data, protocol=V1_PROTOCOL
    ):
        """Test invocation of a deployed ml function."""
        if not isinstance(data, dict) or (
            "instances" not in data and "inputs" not in data
        ):
            key = "instances" if protocol == V1_PROTOCOL else "inputs"
            data = {key: data}
        plug = _as_model(ref, GetPlugResponseV2).entity.plug
        invoke_resp = await self.rules.plugs_execution.execute_sensor_version(
            plug.name, plug.version, json={"properties": data}
        )
        resp_data = invoke_resp.raw_data or {}
        for key in ["predictions", "outputs"]:
            if key in resp_data:
                return resp_data[key]
        return resp_data

    async def publish(self, ref: FunctionResponse | dict):
        """Publish a deployed function."""
        ref = _as_model(ref, FunctionResponse)
        ws_ref = getattr(ref.entity, "webscript", None)
        if ws_ref:
            return await self.webscripts.publish(ws_ref.name, ws_ref.version)
        plug_ref = getattr(ref.entity, "plug", None)
        if plug_ref:
            return await self.plugs.publish(plug_ref.name, plug_ref.version)

    @retry(reraise=True, stop=stop_after_delay(30), wait=wait_exponential(max=10))
    async def remove(self, ref: FunctionResponse | dict, force=True):
        """Remove a deployed function."""
        ref = _as_model(ref, FunctionResponse)
        ws_ref = getattr(ref.entity, "webscript", None)
        if ws_ref:
            return await self.webscripts.remove_version(
                ws_ref.name, ws_ref.version, query={"force": force}
            )
        plug_ref = getattr(ref.entity, "plug", None)
        if plug_ref:
            return await self.plugs.remove_version(
                plug_ref.name, plug_ref.version, query={"force": force}
            )


def _as_model(ref, _type):
    return TypeAdapter(_type).validate_python(ref)
