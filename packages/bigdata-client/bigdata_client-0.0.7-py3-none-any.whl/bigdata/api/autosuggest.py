from typing import List, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel, field_validator

from bigdata.models.entities import MacroEntity
from bigdata.models.languages import Language
from bigdata.models.parse import EntityTypes, KnowledgeGraphTypes
from bigdata.models.sources import Source
from bigdata.models.topics import Topic


class AutosuggestResponseItem(RootModel[list]):
    root: List[KnowledgeGraphTypes]


class AutosuggestResponse(RootModel[dict]):
    root: dict[str, AutosuggestResponseItem]


class ByIdsResponse(RootModel[dict]):
    root: dict[str, Union[Source, Topic, Language, EntityTypes]]


class AutosuggestRequests(RootModel[list]):
    root: List[str]

    @field_validator("root")
    @classmethod
    def no_duplicates(cls, values):
        if len(values) != len(set(values)):
            raise ValueError("Values must be unique")
        return values


class ByIdsRequestItem(BaseModel):
    key: str
    queryType: str


class ByIdsRequest(RootModel[list]):
    root: List[ByIdsRequestItem]
