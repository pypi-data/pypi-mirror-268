from datetime import time
from typing import Any

from pydantic import UUID4, BaseModel, RootModel

from .models import (
    Alarm,
    Condition,
    Device,
    Interface,
    Node,
    Service,
    Storage,
    Tag,
    TagBase,
    TrafficInfo,
)


class SanetOut(BaseModel):
    elapsed_time: time | None = None
    operation: str | None = None
    result: list[Any] | None = None


class NodesOut(SanetOut):
    result: list[Node] | None = None


class NodeOut(SanetOut):
    result: Node | None = None


class InterfaceOut(SanetOut):
    result: Interface | None = None


class InterfacesOut(SanetOut):
    result: list[Interface] | None = None


class AlarmsOut(RootModel):
    root: list[Alarm] | None = None

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]

    def __len__(self):
        return len(self.root)


class PrimaryConditionStatusChangeOut(SanetOut):
    result: list[tuple] | None = None
    condition_path: str | None = None
    element_name: str | None = None
    element_path: str | None = None
    element_uuid: UUID4 | None = None


class TrafficInterfaceOut(SanetOut):
    result: TrafficInfo | None = None
    element_name: str | None = None
    element_path: str | None = None
    element_uuid: UUID4 | None = None


class StoragesOut(SanetOut):
    result: list[Storage] | None = None


class ServicesOut(SanetOut):
    result: list[Service] | None = None


class DevicesOut(SanetOut):
    result: list[Device] | None = None


class ConditionOut(SanetOut):
    result: list[Condition] | None = None


class TagTreesOut(SanetOut):
    result: list[TagBase] | None = None


class TagsOut(SanetOut):
    result: list[Tag] | None = None
