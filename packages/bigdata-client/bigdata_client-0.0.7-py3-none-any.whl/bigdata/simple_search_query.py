"""
A simplified version of the search query
"""

from dataclasses import dataclass
from typing import Optional, Union

from bigdata.api.search import (
    DiscoveryPanelRequest,
    QueryChunksRequest,
    QueryClustersRequest,
    SavedSearchQueryResponse,
    SaveSearchQueryRequest,
)
from bigdata.constants import SEARCH_PAGE_SIZE
from bigdata.daterange import AbsoluteDateRange, RollingDateRange
from bigdata.models.search import (
    Expression,
    ExpressionTypes,
    FileType,
    SearchPagination,
    SortBy,
)
from bigdata.settings import settings


@dataclass
class SimpleSearchQuery:
    """
    A class to hold the simplified search filters.
    For internal use only
    """

    date_range: Optional[Union[AbsoluteDateRange, RollingDateRange]] = None
    keywords: Optional[list[str]] = None
    entities: Optional[list[str]] = None
    sources: Optional[list[str]] = None
    topics: Optional[list[str]] = None
    languages: Optional[list[str]] = None
    watchlists: Optional[list[str]] = None
    sortby: SortBy = SortBy.RELEVANCE
    scope: FileType = FileType.ALL

    def make_copy(self) -> "SimpleSearchQuery":
        return SimpleSearchQuery(
            date_range=self.date_range,
            keywords=list(self.keywords) if self.keywords else None,
            entities=list(self.entities) if self.entities else None,
            sources=list(self.sources) if self.sources else None,
            topics=list(self.topics) if self.topics else None,
            languages=list(self.languages) if self.languages else None,
            watchlists=list(self.watchlists) if self.watchlists else None,
            sortby=self.sortby,
            scope=self.scope,
        )

    def to_query_clusters_api_request(self, page: int) -> QueryClustersRequest:
        """
        Used when composing the request to perform a search using the
        /query-clusters endpoint.
        The difference between this method and to_save_search_request is that
        this one includes the date range in the expression and not outside
        """
        expression = self._build_expression(
            date_range=self.date_range,
            keywords=self.keywords,
            entities=self.entities,
            sources=self.sources,
            topics=self.topics,
            languages=self.languages,
            watchlists=self.watchlists,
        )
        return QueryClustersRequest(
            sort=self.sortby,
            scope=self.scope,
            ranking=settings.LLM.RANKING,
            pagination=SearchPagination(limit=SEARCH_PAGE_SIZE, cursor=page),
            hybrid=settings.LLM.USE_HYBRID,
            expression=expression,
        )

    def to_query_chunks_api_request(self, page: int) -> QueryChunksRequest:
        """
        Used when composing the request to perform a search using the
        /query-chunks endpoint.
        The difference between this method and to_save_search_request is that
        this one includes the date range in the expression and not outside
        """
        expression = self._build_expression(
            date_range=self.date_range,
            keywords=self.keywords,
            entities=self.entities,
            sources=self.sources,
            topics=self.topics,
            languages=self.languages,
            watchlists=self.watchlists,
        )
        return QueryChunksRequest(
            sort=self.sortby,
            scope=self.scope,
            ranking=settings.LLM.RANKING,
            pagination=SearchPagination(limit=SEARCH_PAGE_SIZE, cursor=page),
            hybrid=settings.LLM.USE_HYBRID,
            expression=expression,
        )

    def to_discovery_panel_api_request(self) -> DiscoveryPanelRequest:
        """
        Used when composing the request to get comentions. Pretty much the same
        as to_query_chunks_api_request but without dates
        """
        expression = self._build_expression(
            # This request does not include the date range
            date_range=None,
            keywords=self.keywords,
            entities=self.entities,
            sources=self.sources,
            topics=self.topics,
            languages=self.languages,
            watchlists=self.watchlists,
        )
        return DiscoveryPanelRequest(
            sort=self.sortby,
            scope=self.scope,
            ranking=settings.LLM.RANKING,
            hybrid=settings.LLM.USE_HYBRID,
            expression=expression,
        )

    def to_save_search_request(self) -> SaveSearchQueryRequest:
        """
        Used when composing the request to create a search.
        The difference between this method and to_query_chunks_api_request is that
        this one does not include the date range in the expression but outside
        """
        expression = self._build_expression(
            # Do not include the date range in the expression
            date_range=None,
            keywords=self.keywords,
            entities=self.entities,
            sources=self.sources,
            topics=self.topics,
            languages=self.languages,
            watchlists=self.watchlists,
        )
        date_expression = self._date_range_to_date_expression(self.date_range)
        date_expression = [date_expression] if date_expression is not None else None
        return SaveSearchQueryRequest(
            sort=self.sortby,
            scope=self.scope,
            ranking=settings.LLM.RANKING,
            hybrid=settings.LLM.USE_HYBRID,
            expression=expression,
            date=date_expression,
        )

    @classmethod
    def from_saved_search_response(
        cls, search_query: SavedSearchQueryResponse
    ) -> "SimpleSearchQuery":
        """
        Deserializes a request/response object into a SimpleSearchQuery object,
        if possible
        """
        date_range_raw: Union[list, str] = cls._get_field(
            search_query, ExpressionTypes.DATE
        )
        date_range = cls._date_expression_to_date_range(date_range_raw)
        if date_range is None and search_query.date is not None:
            if len(search_query.date) != 1:
                raise ValueError(
                    "Unexpected error. The date expression should have 1 value"
                )
            expression = search_query.date[0]
            date_range_raw = [
                e
                for e in cls._get_field_from_expression(
                    expression, ExpressionTypes.DATE
                )
                if e is not None
            ]
            if date_range_raw is not None and len(date_range_raw) == 1:
                date_range = cls._date_expression_to_date_range(date_range_raw[0])

        return cls(
            date_range=date_range,
            keywords=cls._get_field(search_query, ExpressionTypes.KEYWORD),
            entities=cls._get_field(search_query, ExpressionTypes.ENTITY),
            sources=cls._get_field(search_query, ExpressionTypes.SOURCE),
            topics=cls._get_field(search_query, ExpressionTypes.TOPIC),
            languages=cls._get_field(search_query, ExpressionTypes.LANGUAGE),
            watchlists=cls._get_field_to_list(search_query, ExpressionTypes.WATCHLIST),
            sortby=search_query.sort,
        )

    def _build_expression(
        self,
        date_range: Optional[Union[AbsoluteDateRange, RollingDateRange]],
        keywords: Optional[list[str]],
        entities: Optional[list[str]],
        sources: Optional[list[str]],
        topics: Optional[list[str]],
        languages: Optional[list[str]],
        watchlists: Optional[list[str]],
    ) -> "Expression":
        expressions = [
            Expression.new(ExpressionTypes.KEYWORD, keywords),
            Expression.new(ExpressionTypes.ENTITY, entities),
            Expression.new(ExpressionTypes.SOURCE, sources),
            Expression.new(ExpressionTypes.TOPIC, topics),
            Expression.new(ExpressionTypes.LANGUAGE, languages),
            # Watchlists is not a list:
            # Expression.new(ExpressionTypes.WATCHLIST, watchlists),
        ]
        for watchlist in watchlists or []:
            expressions.append(Expression.new(ExpressionTypes.WATCHLIST, watchlist))
        expressions = [e for e in expressions if e]
        if date_range is not None:
            expression = self._build_date_range_expression(date_range)
            expressions.append(expression)
        expression = Expression(
            type=ExpressionTypes.AND,
            value=expressions,
        )

        return expression

    @staticmethod
    def _build_date_range_expression(
        date_range: Union[AbsoluteDateRange, RollingDateRange]
    ):
        if isinstance(date_range, RollingDateRange):
            return Expression(type=ExpressionTypes.DATE, value=date_range.value)
        elif isinstance(date_range, AbsoluteDateRange):
            start, end = date_range.to_string_tuple()
            return Expression(
                type=ExpressionTypes.DATE,
                value=[start, end],
            )
        else:
            # This should never happen
            raise ValueError(f"Wrong type sent for date range '{date_range}'")

    @classmethod
    def _get_field(
        cls, search_query: SavedSearchQueryResponse, expression_type: ExpressionTypes
    ):
        fields = cls._get_field_from_expression(
            search_query.expression, expression_type
        )
        fields = list(fields)
        if not fields:
            return None
        if len(fields) != 1:
            raise ValueError(
                f"Unexpected error. The expression should have 1 value of {expression_type}, but it has {len(fields)}"
            )
        return fields[0]

    @classmethod
    def _get_field_to_list(
        cls, search_query: SavedSearchQueryResponse, expression_type: ExpressionTypes
    ):
        """Used for cases like watchlists, which are expressed as multiple objects"""
        fields = cls._get_field_from_expression(
            search_query.expression, expression_type
        )
        if fields is None:
            return None
        return list(fields) or None

    @classmethod
    def _get_field_from_expression(
        cls, expression: Union[Expression, str], expression_type: ExpressionTypes
    ) -> Optional[Union[list, str]]:
        # It should always be a list, because it either comes from the
        # "expression" field or from the values of an AND
        if isinstance(expression, str):
            return None

        if expression.type == expression_type:
            yield expression.value

        if expression.type != ExpressionTypes.AND:
            # We do not support or, not, nor any other type of expression
            # since this should be a simple search query
            return None

        for subexpression in expression.value:
            values = cls._get_field_from_expression(subexpression, expression_type)
            for value in values:
                if value is not None:
                    yield value
        return None

    @staticmethod
    def _date_expression_to_date_range(
        expression: Optional[Expression],
    ) -> Optional[Union[AbsoluteDateRange, RollingDateRange]]:
        if expression is None:
            return None
        if isinstance(expression, list):
            if len(expression) != 2:
                raise ValueError(
                    "Unexpected error. The date expression should have 2 values,"
                    f" but it has {len(expression)}"
                )
            return AbsoluteDateRange(expression[0], expression[1])
        else:
            return RollingDateRange(expression)

    @staticmethod
    def _date_range_to_date_expression(
        date_range: Optional[Union[AbsoluteDateRange, RollingDateRange]]
    ) -> Optional[Expression]:
        if date_range is None:
            return None
        if isinstance(date_range, AbsoluteDateRange):
            start, end = date_range.to_string_tuple()
            return Expression(type=ExpressionTypes.DATE, value=[start, end])
        else:
            return Expression(type=ExpressionTypes.DATE, value=date_range.value)
