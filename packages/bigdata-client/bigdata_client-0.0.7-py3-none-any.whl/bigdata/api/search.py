"""
Models, classes and functions to handle the interaction with the API for the
search functionality.
"""

import datetime
from typing import Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field

from bigdata.constants import SEARCH_PAGE_SIZE
from bigdata.models.entities import (
    Company,
    Concept,
    Facility,
    Landmark,
    Organization,
    OrganizationType,
    Place,
    Product,
    ProductType,
)
from bigdata.models.languages import Language
from bigdata.models.search import (
    Expression,
    FileType,
    Ranking,
    SearchChain,
    SearchPagination,
    SortBy,
)
from bigdata.models.sources import Source
from bigdata.models.story import StoryType
from bigdata.models.topics import Topic
from bigdata.query_type import QueryType
from bigdata.settings import settings

# Save a search


class SaveSearchQueryRequest(BaseModel):
    """Model to represent the "query" attribute of a request to save a search"""

    expression: Expression
    scope: FileType = Field(default=FileType.ALL)
    sort: SortBy = Field(default=SortBy.RELEVANCE)
    ranking: Ranking = Field(default=settings.LLM.RANKING)
    search_chain: Optional[SearchChain] = Field(alias="searchChain", default=None)
    hybrid: bool = settings.LLM.USE_HYBRID
    # The date expression neds a type=ExpressionTypes.DATE
    # the value is coming from date_range.to_expression()
    date: Optional[list[Expression]] = None


class SaveSearchRequest(BaseModel):
    """Model to represent the request to create a search"""

    name: str
    query: SaveSearchQueryRequest
    save_status: Literal["saved"] = Field(default="saved", alias="saveStatus")


class UpdateSearchRequest(BaseModel):
    """Model to represent the request to update a search"""

    name: Optional[str]
    query: SaveSearchQueryRequest


# Get saved searches


class SavedSearchQueryResponse(BaseModel):
    """
    Model to represent the "query" attribute of a response from getting a saved
    search.
    """

    expression: Expression
    scope: FileType = Field(default=FileType.ALL)
    sort: SortBy = Field(default=SortBy.RELEVANCE)
    ranking: Ranking = Field(default=settings.LLM.RANKING)
    search_chain: Optional[SearchChain] = Field(alias="searchChain", default=None)
    hybrid: bool = settings.LLM.USE_HYBRID
    date: Optional[list[Expression]] = None


class SavedSearchResponse(BaseModel):
    """Model to represent the response from getting a saved search"""

    id: str
    name: str
    query: SavedSearchQueryResponse
    save_status: Literal["saved"] = Field(default="saved", alias="saveStatus")
    # TODO: Add dateCreated, lastExecuted, lastUpdated, owner, ownerName, permissions


# List saved searches


class ListSavedSearchResponse(BaseModel):
    """
    Part of the response from listing saved searches. It represents a single
    saved search, without all the details.
    """

    id: str
    name: str
    owner: str
    save_status: Literal["saved"] = Field(default="saved", alias="saveStatus")
    last_executed: datetime.datetime = Field(alias="lastExecuted")
    date_created: datetime.datetime = Field(alias="dateCreated")
    last_updated: datetime.datetime = Field(alias="lastUpdated")
    pinned: bool
    owner_name: str = Field(alias="ownerName")
    shared: dict


class ListSavedSearchesResponse(BaseModel):
    """Model to represent the response from listing saved searches"""

    results: list[ListSavedSearchResponse]


# Run a search


class QueryClustersRequest(BaseModel):
    """Model to represent a request to run a search"""

    expression: Expression
    scope: FileType = Field(default=FileType.ALL)
    sort: SortBy = Field(default=SortBy.RELEVANCE)
    ranking: Ranking = Field(default=settings.LLM.RANKING)
    pagination: SearchPagination = Field(
        default=SearchPagination(limit=SEARCH_PAGE_SIZE, cursor=1)
    )
    search_chain: Optional[SearchChain] = Field(alias="searchChain", default=None)
    hybrid: bool = settings.LLM.USE_HYBRID


class QueryChunksRequest(BaseModel):
    """Model to represent a request to run a search"""

    expression: Expression
    scope: FileType = Field(default=FileType.ALL)
    sort: SortBy = Field(default=SortBy.RELEVANCE)
    ranking: Ranking = Field(default=settings.LLM.RANKING)
    pagination: SearchPagination = Field(
        default=SearchPagination(limit=SEARCH_PAGE_SIZE, cursor=1)
    )
    search_chain: Optional[SearchChain] = Field(alias="searchChain", default=None)
    hybrid: bool = settings.LLM.USE_HYBRID


class ClusteredStoryResponse(BaseModel):
    """
    Helper class to parse the response from the API.
    It should be used only internally to parse the JSON response from the API,
    and not passed around.
    """

    headline: str = Field(validation_alias="hd")
    id: str
    sentiment: float = Field(validation_alias="sent")
    story_type: StoryType = Field(validation_alias="doctype")
    timestamp: datetime.datetime = Field(validation_alias="ts")

    source_key: str = Field(validation_alias="srcKey")
    source_name: str = Field(validation_alias="srcName")
    source_rank: int
    language: str

    class StoryResponseSentence(BaseModel):
        text: str
        pnum: int
        snum: int

        class StoryResponseEntity(BaseModel):
            key: str
            start: int
            end: int
            queryType: QueryType

        entities: list[StoryResponseEntity]

    sentences: list[StoryResponseSentence]


class ChunkedStoryResponse(BaseModel):
    """
    Helper class to parse the response from the API.
    It should be used only internally to parse the JSON response from the API,
    and not passed around.
    """

    headline: str = Field(validation_alias="hd")
    id: str
    sentiment: float = Field(validation_alias="sent")
    story_type: StoryType = Field(validation_alias="doctype")
    timestamp: datetime.datetime = Field(validation_alias="ts")

    source_key: str = Field(validation_alias="srcKey")
    source_name: str = Field(validation_alias="srcName")
    source_rank: int
    language: str

    class ChunkedStoryResponseSentence(BaseModel):
        text: str
        cnum: int

        class StoryResponseEntity(BaseModel):
            key: str
            start: int
            end: int
            queryType: QueryType

        entities: list[StoryResponseEntity]

        class StoryResponseSentence(BaseModel):
            pnum: int
            snum: int

        sentences: list[StoryResponseSentence]

    chunks: list[ChunkedStoryResponseSentence]


class QueryClustersResponse(BaseModel):
    """Model to represent the response from running a search"""

    count: int
    document_count: int = Field(alias="documentCount")
    coverage: dict  # Not worth to model this yet
    timing: dict  # Not worth to model this yet
    stories: list[ClusteredStoryResponse]
    next_cursor: Optional[int] = Field(alias="nextCursor", default=None)


class QueryChunksResponse(BaseModel):
    """Model to represent the response from running a search"""

    count: int
    document_count: int = Field(alias="documentCount")
    coverage: dict  # Not worth to model this yet
    timing: dict  # Not worth to model this yet
    stories: list[ChunkedStoryResponse]
    next_cursor: Optional[int] = Field(alias="nextCursor", default=None)


# Comentions


class DiscoveryPanelRequest(BaseModel):
    """Model to represent a request to get comentions"""

    expression: Expression
    scope: FileType = Field(default=FileType.ALL)
    sort: SortBy = Field(default=SortBy.RELEVANCE)
    ranking: Ranking = Field(default=settings.LLM.RANKING)
    search_chain: Optional[SearchChain] = Field(alias="searchChain", default=None)
    hybrid: bool = settings.LLM.USE_HYBRID


class DiscoveryPanelResponse(BaseModel):
    """Model to represent the response from getting comentions"""

    companies: list[Company]
    concepts: list[Concept]
    languages: list[Language]
    organizations: list[Union[Organization, OrganizationType]]
    places: list[Union[Place, Facility, Landmark]]
    products: list[Union[Product, ProductType]]
    sources: list[Source]
    topics: list[Topic]
