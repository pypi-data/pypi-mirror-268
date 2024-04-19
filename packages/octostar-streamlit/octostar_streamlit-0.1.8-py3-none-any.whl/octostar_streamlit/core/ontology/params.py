from dataclasses import dataclass
from typing import Union
from octostar_streamlit.core.entities import Entity, Relationship
from octostar_streamlit.core.params_base_model import ParamsBaseModel


class CancelQueriesParams(ParamsBaseModel):
    context: str


class GetWorkspaceRelationshipRecordsParams(ParamsBaseModel):
    entity: Entity
    relationship: Union[str, Relationship]


class ClearRelationshipCacheParams(ParamsBaseModel):
    entity: Entity
    relationship: Union[str, Relationship]


class GetConnectedEntitiesParams(ParamsBaseModel):
    entity: Entity
    relationship: Union[str, Relationship]
    force_refresh: Union[
        bool, None
    ]  # TODO: add alias to automatically convert to camelCase


class GetConceptByNameParams(ParamsBaseModel):
    concept_name: str  # TODO: add alias to automatically convert to camelCase


class GetEntityParams(ParamsBaseModel):
    entity: Entity
    refresh: Union[bool, None] = None
    skip_side_effects: Union[bool, None] = (
        None  # TODO: add alias to automatically convert to camelCase
    )


class GetRelationshipCountParams(ParamsBaseModel):
    entity: Entity
    relationship: Union[str, Relationship]
    force_refresh: Union[
        bool, None
    ]  # TODO: add alias to automatically convert to camelCase


class GetConceptForEntityparams(ParamsBaseModel):
    entity: Entity


class GetRelationshipForEntityParams(ParamsBaseModel):
    entity: Entity


@dataclass
class SendQueryOptions:
    context: Union[str, None] = None
    low_priority: Union[bool, None] = None


class SendQueryParams(ParamsBaseModel):
    query: str
    options: Union[SendQueryOptions, None] = None


class ConsistentUUIDParams(ParamsBaseModel):
    name: str
    namespace: Union[str, None] = None
