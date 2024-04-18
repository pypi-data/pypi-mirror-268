from dataclasses import dataclass
from typing import Iterable, Iterator, Optional, Union

from bigdata.advanced_search_query import AdvancedSearchQuery
from bigdata.api.search import (
    QueryChunksResponse,
    QueryClustersResponse,
    SavedSearchResponse,
    SaveSearchRequest,
    UpdateSearchRequest,
)
from bigdata.connection import BigdataConnection
from bigdata.constants import MAX_SEARCH_PAGES
from bigdata.daterange import AbsoluteDateRange, RollingDateRange
from bigdata.models.advanced_search_query import QueryComponent
from bigdata.models.comentions import Comentions
from bigdata.models.search import FileType, SortBy
from bigdata.simple_search_query import SimpleSearchQuery
from bigdata.story import Story


class Search:
    """
    Class representing a search, saved or not.
    It allows you to perform searches.
    """

    def __init__(
        self,
        api: BigdataConnection,
        # TODO: Change the type of this to something more generic
        query: "SimpleSearchQuery",
        id: Optional[str] = None,
        name: str = "",
    ):
        self.api: BigdataConnection = api
        self.id: Optional[str] = id
        self.name: str = name
        self.query: SimpleSearchQuery = query or SimpleSearchQuery()

    @classmethod
    def from_filters(
        cls,
        api: "BigdataConnection",
        date_range: Optional[Union[AbsoluteDateRange, RollingDateRange]] = None,
        keywords: Optional[list[str]] = None,
        entities: Optional[list[str]] = None,
        sources: Optional[list[str]] = None,
        topics: Optional[list[str]] = None,
        languages: Optional[list[str]] = None,
        watchlists: Optional[list[str]] = None,
        sortby: SortBy = SortBy.RELEVANCE,
        scope: FileType = FileType.ALL,
    ) -> "Search":
        """Create a simplified search with just a set of filters"""
        rpx_query = SimpleSearchQuery(
            date_range=date_range,
            keywords=keywords,
            entities=entities,
            sources=sources,
            topics=topics,
            languages=languages,
            watchlists=watchlists,
            sortby=sortby,
            scope=scope,
        )
        return cls(api=api, query=rpx_query)

    @classmethod
    def from_query(
        cls,
        api: "BigdataConnection",
        query: QueryComponent,
        date_range: Optional[Union[AbsoluteDateRange, RollingDateRange]] = None,
        sortby: SortBy = SortBy.RELEVANCE,
        scope: FileType = FileType.ALL,
    ) -> "Search":
        """Create a simplified search with just a set of filters"""
        rpx_query = AdvancedSearchQuery(
            date_range=date_range, query=query, sortby=sortby, scope=scope
        )
        return cls(api=api, query=rpx_query)

    @classmethod
    def from_saved_search_response(
        cls, api: BigdataConnection, response: SavedSearchResponse
    ):
        simple_query = SimpleSearchQuery.from_saved_search_response(response.query)

        return cls(
            api=api,
            query=simple_query,
            id=response.id,
            name=response.name,
            # TODO: Add the rest of the parameters like created_at, updated_at,
            # owner, etc.
        )

    def limit_stories(self, limit: int) -> Iterable[Story]:
        """Limit the number of stories returned by this search"""
        new = self.make_copy()
        return SearchResults(new, limit=limit)

    def get_comentions(self) -> Comentions:
        if self.api is None:
            raise ValueError("The search object must have an API to get comentions.")
        request = self.query.to_discovery_panel_api_request()
        response = self.api.query_discovery_panel(request)
        return Comentions.from_response(response)

    def make_copy(self):
        query = self.query.make_copy()
        return Search(self.api, id=self.id, name=self.name, query=query)

    def get_page(self, page: int = 1) -> QueryChunksResponse:
        if self.api is None:
            raise ValueError("The search object must have an API to get pages.")
        request = self.query.to_query_chunks_api_request(page)
        return self.api.query_chunks(request)

    def save(self, name: str):
        if self.api is None:
            raise ValueError("The search object must have an API to save.")
        if self.id is None:
            # Create a new search
            request = SaveSearchRequest(
                name=name, query=self.query.to_save_search_request()
            )
            response = self.api.save_search(request)
            self.id = response["id"]
        else:
            # Update an existing search
            request = UpdateSearchRequest(
                name=name, query=self.query.to_save_search_request()
            )
            response = self.api.update_search(request, self.id)

    def delete(self):
        if self.api is None:
            raise ValueError("The search object must have an API to delete.")
        if self.id is None:
            raise ValueError("The search object is not saved.")
        self.api.delete_search(self.id)
        self.id = None

    @property
    def is_saved(self) -> bool:
        return self.id is not None


# To be changed. It shouldn't be a dataclass, but for now it's fine
@dataclass
class SearchResults:
    """
    A search with a limit. It allows you to get the count of stories, and/or get
    an iterator over the results.
    """

    def __init__(self, search: Search, limit: int):
        self.search = search
        self._first_page: Optional[QueryClustersResponse] = None
        if limit <= 0:
            raise ValueError("The limit must be a positive number.")
        self._limit_stories = limit

    @property
    def _sentence_count(self) -> int:
        """
        INTERNAL!!
        Do not rely on this because it may not mean what you think it means, and
        could change.
        """
        first_page = self._ensure_first_page()
        return first_page.count

    @property
    def _document_count(self) -> int:
        """
        INTERNAL!!
        Do not rely on this because it may not mean what you think it means.
        """
        first_page = self._ensure_first_page()
        return first_page.document_count

    def _ensure_first_page(self) -> QueryClustersResponse:
        if self._first_page is None:
            self._first_page = self.search.get_page()
        return self._first_page

    def __iter__(self) -> Iterable[Story]:
        return iter(
            SearchResultsPaginatorIterator(
                self.search, self._limit_stories, self._first_page
            )
        )


class SearchResultsPaginatorIterator:
    """
    Helper to iterate over the stories in all the pages.
    Optionally, it can skip the first request and use the first_page parameter.
    """

    def __init__(
        self,
        search: Search,
        limit_stories: int,
        first_page: Optional[QueryClustersResponse],
    ):
        self.search = search
        self.current_page = first_page or None
        self._limit_stories = limit_stories
        self._page_num = 0

    def __iter__(self) -> Iterator[Story]:
        # The first page may have been provided, if the user asked for the count first
        if self.current_page is None:
            self.current_page = self.search.get_page()
        items = 0
        for _ in range(MAX_SEARCH_PAGES):  # Effectively a while(True), but safer
            for story in self.current_page.stories:
                if items >= self._limit_stories:
                    return
                items += 1
                yield Story.from_response(story)
            next_page = self.current_page.next_cursor
            if not next_page:
                break
            self._page_num = next_page
            self.current_page = self.search.get_page(self._page_num)
