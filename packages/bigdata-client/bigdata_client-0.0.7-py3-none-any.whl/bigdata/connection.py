from typing import Generator, TypeVar, Union
from urllib.parse import urljoin

from pydantic import BaseModel, ValidationError

from bigdata.api.autosuggest import (
    AutosuggestRequests,
    AutosuggestResponse,
    AutosuggestResponseItem,
    ByIdsRequest,
    ByIdsResponse,
)
from bigdata.api.search import (
    DiscoveryPanelRequest,
    DiscoveryPanelResponse,
    ListSavedSearchesResponse,
    QueryChunksRequest,
    QueryChunksResponse,
    SavedSearchResponse,
    SaveSearchRequest,
    UpdateSearchRequest,
)
from bigdata.auth import AsyncRequestContext, AsyncResponseContext, Auth

CONCURRENT_AUTOSUGGEST_REQUESTS_LIMIT = 10


class AsyncRequestPartialContext(BaseModel):
    """
    Context used to pass information to connection module for making async requests.
    Async requests are made in parallel, so each request is associated with an id to
    retrieve it from a list of responses.
    """

    id: str
    endpoint: str
    params: dict


json_types = Union[dict, list[dict]]

T = TypeVar("T")


class BigdataConnection:
    """
    The connection to the API.

    Contains the Auth object with the JWT and abstracts all the calls to the API,
    receiving and returning objects to/from the caller.
    For internal use only.
    """

    def __init__(self, auth: Auth, api_url: str):
        self.http = HTTPWrapper(auth, api_url)

    # Autosuggest

    def autosuggest(
        self, items: AutosuggestRequests, limit: int
    ) -> AutosuggestResponse:
        """Calls GET /autosuggest"""

        # Split the requests in batches of size CONCURRENT_AUTOSUGGEST_REQUESTS_LIMIT to not overload the service
        all_requests_input = [
            AsyncRequestPartialContext(
                id=item,
                endpoint="autosuggest",
                params={"query": item, "limit": limit},
            )
            for item in items.root
        ]

        responses = []
        for batch in self._get_batches(
            all_requests_input, CONCURRENT_AUTOSUGGEST_REQUESTS_LIMIT
        ):
            responses.extend(self.http.async_get(batch))

        return AutosuggestResponse(
            root={
                item.id: AutosuggestResponseItem(root=item.response["results"])
                for item in responses
            }
        )

    @staticmethod
    def _get_batches(items: list[T], batch_size: int) -> Generator[list[T], None, None]:
        for idx in range(0, len(items), batch_size):
            yield items[idx : idx + batch_size]

    def by_ids(self, request: ByIdsRequest) -> ByIdsResponse:
        json_request = request.model_dump(exclude_none=True, by_alias=True)
        json_response = self.http.post("cqs/by-ids", json=json_request)
        return ByIdsResponse(root=json_response)

    # Search

    def query_chunks(self, request: QueryChunksRequest) -> QueryChunksResponse:
        """Calls POST /cqs/query-chunks"""
        json_request = request.model_dump(exclude_none=True, by_alias=True)
        json_response = self.http.post("cqs/query-chunks", json=json_request)
        return QueryChunksResponse(**json_response)

    def get_search(self, id: str) -> SavedSearchResponse:
        """Calls GET /user-data/queries/{id}"""
        json_response = self.http.get(f"user-data/queries/{id}")
        try:
            return SavedSearchResponse(**json_response)
        except ValidationError as e:
            raise NotImplementedError(
                "Query expression may have unsupported expression types"
            ) from e

    def list_searches(
        self, saved: bool = True, owned: bool = True
    ) -> ListSavedSearchesResponse:
        """Calls GET /user-data/queries"""
        params = {}
        if saved:
            params["save_status"] = "saved"
        if owned:
            params["owned"] = "true"
        json_response = self.http.get("user-data/queries", params=params)
        return ListSavedSearchesResponse(**json_response)

    def save_search(self, request: SaveSearchRequest) -> dict:
        """Calls POST /user-data/queries"""
        json_request = request.model_dump(exclude_none=True, by_alias=True)
        return self.http.post("user-data/queries", json=json_request)

    def update_search(self, request: UpdateSearchRequest, search_id: str) -> dict:
        """Calls PATCH /user-data/queries/{id}"""
        json_request = request.model_dump(exclude_none=True, by_alias=True)
        return self.http.patch(f"user-data/queries/{search_id}", json=json_request)

    def delete_search(self, id: str) -> dict:
        """Calls DELETE /user-data/queries/{id}"""
        return self.http.delete(f"user-data/queries/{id}")

    def query_discovery_panel(
        self, request: DiscoveryPanelRequest
    ) -> DiscoveryPanelResponse:
        """Calls POST /cqs/discovery-panel"""
        json_request = request.model_dump(exclude_none=True, by_alias=True)
        json_response = self.http.post("cqs/discovery-panel", json=json_request)
        return DiscoveryPanelResponse(**json_response)


class HTTPWrapper:
    """
    A basic connection to perform HTTP GET, POST, PATCH, DELETE requests.
    """

    def __init__(self, auth: Auth, api_url: str):
        self.auth = auth
        self.api_url = api_url

    def get(self, endpoint: str, params: dict = None) -> dict:
        params = params or {}
        url = self._get_url(endpoint)
        response = self.auth.request("GET", url, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint: str, json: json_types) -> json_types:
        url = self._get_url(endpoint)
        response = self.auth.request("POST", url, json=json)
        response.raise_for_status()
        return response.json()

    def patch(self, endpoint: str, json: json_types) -> json_types:
        url = self._get_url(endpoint)
        response = self.auth.request("PATCH", url, json=json)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint: str) -> json_types:
        url = self._get_url(endpoint)
        response = self.auth.request("DELETE", url)
        response.raise_for_status()
        return response.json()

    # Async wrappers for HTTP methods
    def async_get(
        self, async_partial_contexts: list[AsyncRequestPartialContext]
    ) -> list[AsyncResponseContext]:
        all_requests_context = [
            AsyncRequestContext(
                id=partial_context.id,
                url=self._get_url(partial_context.endpoint),
                params=partial_context.params,
            )
            for partial_context in async_partial_contexts
        ]
        response = self.auth.async_requests("GET", all_requests_context)
        return response

    # Other helpers

    def _get_url(self, endpoint: str) -> str:
        return urljoin(str(self.api_url), str(endpoint))
