from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from bigdata.models.advanced_search_query import QueryComponent
from bigdata.models.advanced_search_query import Watchlist as WatchlistQuery
from bigdata.models.search import Expression


class Watchlist(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str = Field(validation_alias="key")
    name: str
    query_type: Literal["watchlist"] = Field(
        default="watchlist", validation_alias="queryType"
    )

    # QueryComponent methods

    @property
    def _query_proxy(self):
        return WatchlistQuery(self.id)

    def to_expression(self) -> Expression:
        return self._query_proxy.to_expression()

    def __or__(self, other: QueryComponent) -> QueryComponent:
        return self._query_proxy | other

    def __and__(self, other: QueryComponent) -> "And":
        return self._query_proxy & other

    def __invert__(self) -> "Not":
        return ~self._query_proxy

    def make_copy(self) -> "QueryComponent":
        return self._query_proxy.make_copy()
