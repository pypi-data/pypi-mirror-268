import logging
from datetime import datetime

import requests
from pydantic import validate_call

from .core import SanetId, sanetapi
from .schemas.models import NodesDict
from .schemas.outs import (
    AlarmsOut,
    ConditionOut,
    DevicesOut,
    InterfaceOut,
    InterfacesOut,
    NodeOut,
    NodesOut,
    PrimaryConditionStatusChangeOut,
    ServicesOut,
    StoragesOut,
    TagsOut,
    TagTreesOut,
    TrafficInterfaceOut,
)
from .settings import SanetSettings

logger = logging.getLogger(__name__)


class SanetApi:
    def __init__(self, settings: SanetSettings):
        self.settings = settings

    @property
    def auth_token_parameter(self):
        return "sanet3auth"

    @property
    def auth_data(self):
        return {self.auth_token_parameter: self.settings.auth_token.get_secret_value()}

    def call_api(
        self,
        method: str,
        path: str,
        params: dict | None = None,
        headers: dict | None = None,
        data: dict | str | None = None,
        **kwargs,
    ):
        url = f"{self.settings.api_url}{path}"
        request_method = getattr(requests, method)
        response = request_method(
            url, headers=headers, data=data, params=params, **kwargs
        )

        return response

    @sanetapi(schema_out=NodesOut)
    def read_all_nodes(
        self,
        **kwargs,
    ) -> NodesOut:
        result = self.call_api("get", "nodes", **kwargs)
        return result

    @validate_call
    @sanetapi(schema_out=NodeOut)
    def read_node(
        self,
        node_id: SanetId,
        **kwargs,
    ) -> NodeOut:
        result = self.call_api("get", f"node/{node_id}", **kwargs)
        return result

    @validate_call
    @sanetapi(schema_out=PrimaryConditionStatusChangeOut)
    def read_primary_condition_status_change(
        self,
        node_id: SanetId,
        start: datetime | None = None,
        end: datetime | None = None,
        **kwargs,
    ) -> PrimaryConditionStatusChangeOut:
        if start:
            kwargs["params"].update({"ts_start": int(start.timestamp())})
        if end:
            kwargs["params"].update({"ts_end": int(end.timestamp())})
        result = self.call_api(
            "get",
            f"node/{node_id}/get_primary_condition_status_change",
            **kwargs,
        )
        return result

    @sanetapi(schema_out=AlarmsOut)
    def read_all_alarms(
        self,
        priority_level: str | None = None,
        **kwargs,
    ) -> AlarmsOut:
        result = self.call_api("get", "alarm/current", **kwargs)
        return result

    @sanetapi(schema_out=InterfacesOut)
    def read_all_interfaces(
        self,
        **kwargs,
    ) -> InterfacesOut:
        result = self.call_api("get", "interfaces", **kwargs)
        return result

    @validate_call
    @sanetapi(schema_out=InterfaceOut)
    def read_interface(
        self,
        interface_id: SanetId,
        **kwargs,
    ) -> InterfaceOut:
        result = self.call_api("get", f"interface/{interface_id}", **kwargs)
        return result

    @validate_call
    @sanetapi(schema_out=TrafficInterfaceOut)
    def read_traffic_interface(
        self,
        interface_id: SanetId,
        ts_start: int | None = None,
        ts_end: int | None = None,
        **kwargs,
    ) -> TrafficInterfaceOut:
        result = self.call_api("get", f"interface/{interface_id}/get_traffic", **kwargs)
        return result

    @sanetapi(schema_out=StoragesOut)
    def read_all_storages(
        self,
        **kwargs,
    ) -> StoragesOut:
        result = self.call_api("get", "storages", **kwargs)
        return result

    @sanetapi(schema_out=ServicesOut)
    def read_all_services(
        self,
        **kwargs,
    ) -> ServicesOut:
        result = self.call_api("get", "services", **kwargs)
        return result

    @sanetapi(schema_out=DevicesOut)
    def read_all_devices(
        self,
        **kwargs,
    ) -> DevicesOut:
        result = self.call_api("get", "devices", **kwargs)
        return result

    @sanetapi(schema_out=ConditionOut)
    def read_all_conditions(
        self,
        **kwargs,
    ) -> ConditionOut:
        result = self.call_api("get", "conditions", **kwargs)
        return result

    @sanetapi(schema_out=TagTreesOut)
    def read_tagtrees(
        self,
        **kwargs,
    ) -> TagTreesOut:
        result = self.call_api("get", "tagtrees", **kwargs)
        return result

    @sanetapi(schema_out=TagsOut)
    def read_all_tags(
        self,
        **kwargs,
    ) -> TagsOut:
        result = self.call_api("get", "tags", **kwargs)
        return result


def read_all_nodes(api: SanetApi, key: str = "name") -> NodesDict:
    results = api.read_all_nodes()
    return NodesDict.create(nodes=results.result, key=key)
