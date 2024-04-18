from datetime import datetime
from typing import Any

from pydantic import (
    UUID4,
    BaseModel,
    ConfigDict,
    RootModel,
    computed_field,
    validate_call,
)
from pydantic.networks import IPvAnyAddress, IPvAnyNetwork

from ..enums import ElementType, PriorityLevel


class SanetBase(BaseModel):
    name: str | None = None
    path: str | None = None
    uuid: UUID4 | None = None


class SanetModel(SanetBase):
    cluster_distinguisher: str | None = None
    cluster_element_id: UUID4 | None = None
    cluster_instance: str | None = None
    cluster_instance_time: datetime | None = None  # TODO: verificare
    cluster_role: int | None = None
    cluster_xform: str | None = None
    cluster_id: UUID4 | None = None
    description: str | None = None
    kind: int | None = None
    parent_id: str | None = None
    tenant_id: UUID4 | None = None


class SanetComponentModel(SanetModel):
    distinguisher: str | None = None
    is_abstract: bool | None = None
    xform: str | None = None


class Node(SanetModel):
    model_config = ConfigDict(extra="allow")

    agent_id: UUID4 | None = None
    dft_timeout: int | None = None
    dns6_name: str | None = None
    dns_name: str | None = None
    effective_ip: IPvAnyAddress | None = None
    ip4_mgt: str | None = None
    ip6_mgt: str | None = None
    is_abstract: bool = False
    snmp_community: str | None = None
    snmp_port: int | None = None
    snmp_v3_authdata: str | None = None
    snmp_version: int | None = None
    timezone: str | None = None
    use_ipv4: bool = True

    @validate_call
    def is_in_subnet(self, subnet: IPvAnyNetwork):
        return self.effective_ip in subnet


class NodesDict(RootModel):
    root: dict[str, Node] = {}

    def __iter__(self):
        return iter(self.root)

    @validate_call
    def __getitem__(self, item: str) -> Node:
        return self.root[item]

    @validate_call
    def __contains__(self, key) -> bool:
        return key in self.root

    @validate_call
    def __setitem__(self, item: str, value: Node):
        self.root[item] = value

    def keys(self):
        return self.root.keys()

    @classmethod
    def create(cls, nodes: list[Node], key: str = "name") -> "NodesDict":
        data = {}
        for node in nodes:
            data[str(getattr(node, key))] = node
        return cls(data)


class Interface(SanetComponentModel):
    model_config = ConfigDict(extra="forbid")

    backbone: bool | None = None
    ifindex: str | None = None
    speed: float | None = None


class Storage(SanetComponentModel):
    model_config = ConfigDict(extra="forbid")

    stindex: str | None = None


class Service(SanetComponentModel):
    model_config = ConfigDict(extra="forbid")

    swrunindex: str | None = None


class Device(SanetComponentModel):
    model_config = ConfigDict(extra="forbid")

    devindex: str | None = None


class Element(SanetBase):
    model_config = ConfigDict(extra="forbid", validate_assignment=True)

    _base_url: str = ""

    description: str | None = None
    parent_id: UUID4 | None = None
    parent_name: str | None = None
    # *tipo dell'elemento (1=nodo,2=interfaccia,3=storage,4=service,5=device)*
    type: ElementType | None = None

    @computed_field  # type: ignore[misc]
    def absolute_url(self) -> str:
        return f"{self.type.name.lower()}/{self.uuid.hex}"

    @computed_field  # type: ignore[misc]
    def absolute_parent_url(self) -> str:
        return f"{ElementType.NODE.name.lower()}/{self.parent_id.hex}" if self.parent_id else ""

    def is_node(self):
        return self.type == ElementType.NODE


class ConditionBase(SanetBase):
    priority: int | None = None
    classification: str | None = None
    statuslastchange: datetime | None = None


class Condition(ConditionBase):
    model_config = ConfigDict(extra="forbid")

    statuschange_action: str | None = None
    uncheckable_fallback: int | None = None
    primary: bool | None = None
    mtime: datetime | None = None
    statuslast: Any | None = None
    lastchecktotaltime: Any | None = None  # TODO: verificare
    title: str | None = None
    element_id: UUID4 | None = None
    status: int | None = None
    tries: int | None = None
    passive_force_status: str | None = None
    max_tries: int | None = None
    dependson_id: str | None = None
    expr: str | None = None
    cascade: bool | None = None
    datagroup_id: UUID4 | None = None
    lastdone: int | None = None
    order: int | None = None


class AlarmCondition(ConditionBase):
    model_config = ConfigDict(extra="forbid")

    priority_level: PriorityLevel | None = None
    description: str | None = None


class Result(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: int | None = None
    laststatus: int | None = None


class Cluster(BaseModel):
    model_config = ConfigDict(extra="allow")

    name: list[str] | str | None = None


class Alarm(BaseModel):
    model_config = ConfigDict(extra="allow")

    info: dict | None = None
    datasources: dict | None = None
    tags: list[str] | None = None
    element: Element | None = None
    meta: dict | None = None
    result: Result | None = None
    condition: AlarmCondition | None = None
    cluster: Cluster | None = None


class TagBase(SanetBase):
    model_config = ConfigDict(extra="forbid")


class Tag(TagBase):
    model_config = ConfigDict(extra="allow")

    icon: str | None = None
    mtime: datetime | None = None
    parent_id: UUID4 | None = None
    tree_id: UUID4 | None = None


class TrafficInfo(BaseModel):
    in_avg: float | None = None
    in_max: float | None = None
    out_avg: float | None = None
    out_max: float | None = None
