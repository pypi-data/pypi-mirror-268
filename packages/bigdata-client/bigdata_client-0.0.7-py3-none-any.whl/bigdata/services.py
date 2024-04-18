import os
from typing import Optional, Union

from bigdata import old_auth
from bigdata.api.autosuggest import (
    AutosuggestRequests,
    AutosuggestResponse,
    ByIdsRequest,
)
from bigdata.auth import Auth
from bigdata.connection import BigdataConnection
from bigdata.daterange import AbsoluteDateRange, RollingDateRange
from bigdata.models.advanced_search_query import QueryComponent
from bigdata.models.entities import MacroEntity
from bigdata.models.languages import Language
from bigdata.models.parse import (
    AutosuggestedSavedSearch,
    EntityTypes,
    KnowledgeGraphTypes,
)
from bigdata.models.search import FileType, SortBy
from bigdata.models.sources import Source
from bigdata.models.topics import Topic
from bigdata.models.uploads import Document, UploadQuota
from bigdata.models.watchlists import Watchlist
from bigdata.query_type import QueryType
from bigdata.search import Search
from bigdata.settings import BigdataAuthType, settings

CONCURRENT_AUTOSUGGEST_REQUESTS_LIMIT = 10


class Bigdata:
    """
    Represents a connection to RavenPack's Bigdata API.

    :ivar knowledge_graph: Proxy for the domain search functionality.
    :ivar content_search: Proxy object for the content search functionality.
    :ivar watchlists: Proxy object for the watchlist functionality.
    :ivar uploads: Proxy object for the internal content functionality.
    """

    def __init__(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        auth_type: Optional[BigdataAuthType] = None,
        api_url: Optional[str] = None,
    ):
        if password is None:
            password = os.environ.get("BIGDATA_PASSWORD")
        if username is None:
            username = os.environ.get("BIGDATA_USER")
        if username is None or password is None:
            raise ValueError("Username and password must be provided")
        if auth_type is None:
            auth_type = settings.BIGDATA_AUTH_TYPE
        if auth_type == BigdataAuthType.CLERK:
            auth = Auth.from_username_and_password(username, password)
        else:
            auth = old_auth.Auth.from_username_and_password(username, password)

        if api_url is None:
            api_url = str(settings.BIGDATA_API_URL)
        self.api = BigdataConnection(auth, api_url)
        self.knowledge_graph = KnowledgeGraph(self.api)
        self.content_search = ContentSearch(self.api)
        self.watchlists = Watchlists(self.api)
        self.uploads = Uploads(self.api)


class KnowledgeGraph:
    """For finding entities, sources and topics"""

    def __init__(self, api_connection: BigdataConnection):
        self.api = api_connection

    def autosuggest(
        self, values: list[str], /, limit=20
    ) -> dict[str, list[KnowledgeGraphTypes]]:
        """
        Searches for entities, sources, topics, searches and watchlists
        """

        # TODO update response model returned to dict[str, list[KnowledgeGraphTypes]]
        api_response = self.api.autosuggest(
            AutosuggestRequests(root=values), limit=limit
        )

        # Exclude macros and saved searches from response
        api_response = self._exclude_macros_and_saved_searches(api_response)

        return {key: results.root for key, results in api_response.root.items()}

    @staticmethod
    def _exclude_macros_and_saved_searches(
        api_response: AutosuggestResponse,
    ) -> AutosuggestResponse:
        filtered_response = {}
        for key, key_results in api_response.root.items():
            filtered_response[key] = list(
                filter(
                    lambda result: not isinstance(
                        result, (MacroEntity, AutosuggestedSavedSearch)
                    ),
                    key_results.root,
                )
            )
        return AutosuggestResponse(root=filtered_response)

    def get_entities(self, ids: list[str], /) -> list[EntityTypes]:
        """Retrieve a list of entities by their ids."""
        return self._get_by_ids(ids, QueryType.ENTITY)

    def get_sources(self, ids: list[str], /) -> list[Source]:
        """Retrieve a list of sources by its ids."""
        return self._get_by_ids(ids, QueryType.SOURCE)

    def get_topics(self, ids: list[str], /) -> list[Topic]:
        """Retrieve a list of topics by its ids."""
        return self._get_by_ids(ids, QueryType.TOPIC)

    def get_languages(self, ids: list[str], /) -> list[Language]:
        """Retrieve a list of languages by its ids."""
        return self._get_by_ids(ids, QueryType.LANGUAGE)

    def _get_by_ids(self, ids: list[str], query_type: QueryType) -> list:
        api_response = self.api.by_ids(
            ByIdsRequest.model_validate(
                [{"key": id_, "queryType": query_type} for id_ in ids]
            )
        )
        return [api_response.root.get(id_) for id_ in ids]


class Watchlists:
    def __init__(self, api_connection: BigdataConnection):
        self.api = api_connection

    def get(self, id_, /) -> Watchlist:
        """Retrieve a watchlist by its id."""

    def list(self) -> list[Watchlist]:
        """Retrieve all watchlists for the current user."""

    def create(self, name: str, /) -> Watchlist:
        """Creates a new watchlist in the system."""

    def delete(self, id_, /):
        """Delete a watchlist by its id."""


class ContentSearch:
    def __init__(self, api_connection: BigdataConnection):
        self.api = api_connection

    # Search content

    def new_search(
        self,
        /,
        date_range: Optional[Union[AbsoluteDateRange, RollingDateRange]] = None,
        keywords: Optional[list[str]] = None,
        entities: Optional[list[str]] = None,
        sources: Optional[list[str]] = None,
        topics: Optional[list[str]] = None,
        languages: Optional[list[str]] = None,
        watchlists: Optional[list[str]] = None,
        sortby: Optional[SortBy] = SortBy.RELEVANCE,
        scope: FileType = FileType.ALL,
    ) -> Search:
        """
        Creates a new search object that allows you to perform a search on
        keywords and entity_ids.

        Example usage:

        >>> search = bigdata.content_search.new_search(
        ...    keywords=["tesla"],
        ...    entities=["228D42"]
        ... )                               # doctest: +SKIP
        >>> search.save()                   # doctest: +SKIP
        >>> for story in search.limit(100): # doctest: +SKIP
        >>>     print(story)                # doctest: +SKIP
        >>> print(search.get_summary())     # doctest: +SKIP
        >>> search.delete()                 # doctest: +SKIP
        """
        return Search.from_filters(
            api=self.api,
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

    def new_from_query(
        self,
        query: QueryComponent,
        date_range: Optional[Union[AbsoluteDateRange, RollingDateRange]] = None,
        sortby: SortBy = SortBy.RELEVANCE,
        scope: FileType = FileType.ALL,
    ) -> Search:
        return Search.from_query(
            self.api, query, date_range=date_range, sortby=sortby, scope=scope
        )

    def get(self, id_, /) -> Search:
        """Retrieve a saved search by its id."""
        response = self.api.get_search(id_)
        return Search.from_saved_search_response(self.api, response)

    def list(self) -> list[Search]:
        """Retrieve all saved searches for the current user."""
        list_response = self.api.list_searches()
        searches = []
        for search in list_response.results:
            try:
                response = self.api.get_search(search.id)
            except NotImplementedError as e:
                print(
                    f"Skipping search {search.id} because it has an unsupported expression type"
                )
                continue
            searches.append(Search.from_saved_search_response(self.api, response))
        return searches

    def delete(self, id_, /):
        """Delete a saved search by its id."""
        self.api.delete_search(id_)


class Uploads:
    """For managing internal uploads. Searching will be done through content"""

    def __init__(self, api_connection: BigdataConnection):
        self.api = api_connection

    def get(self, id_, /) -> Document:
        """Retrieve a document by its id."""

    def list(self) -> list[Document]:
        """Retrieve all documents for the current user."""

    def upload_document(self, document: Document, /):
        """Uploads a document to the bigdata platform."""

    def delete(self, id_, /):
        """Delete a document by its id."""

    def get_quota(self) -> UploadQuota:
        """Retrieve the remaining upload quota for the current user."""

    # TODO: add methods to manage folders etc
