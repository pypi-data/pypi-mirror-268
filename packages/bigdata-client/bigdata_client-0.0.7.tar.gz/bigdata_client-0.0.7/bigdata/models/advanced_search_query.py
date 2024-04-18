from abc import ABC, ABCMeta, abstractmethod
from typing import Protocol, Union, runtime_checkable

from bigdata.models.search import Expression, ExpressionOperation, ExpressionTypes


# Decorated with runtime_checkable to allow isinstance checks
@runtime_checkable
class QueryComponent(Protocol):
    """
    Protocol for any query component.
    Any class that implements this protocol should be able to be converted to
    an Expression object, and should be able to operate with other QueryComponents
    """

    def to_expression(self) -> Expression: ...

    def make_copy(self) -> "QueryComponent": ...

    def __and__(self, other: "QueryComponent") -> "QueryComponent": ...

    def __or__(self, other: "QueryComponent") -> "QueryComponent": ...

    def __invert__(self) -> "QueryComponent": ...


class BaseQueryComponent(ABC):
    """
    An abstract component that implements the common basic logic of the query
    components, like the AND, OR, and NOT operators.
    """

    def __and__(self, other: QueryComponent) -> QueryComponent:
        """
        Joins two query components with an AND operator.

        Note: The return type is QueryComponent instead of And because cases like
        Entity("1") & Entity("2") should return
        Entity("1", "2", operation=ExpressionOperation.ALL)
        instead of
        And(Entity("1"), Entity("2"))
        """
        return And(self, other)

    def __or__(self, other: QueryComponent) -> QueryComponent:
        """
        Joins two query components with an OR operator.

        Note: The return type is QueryComponent instead of Or because cases like
        Entity in [1,2] | Entity in [3,4]` should return
        Entity in [1,2,3,4] instead of Or(Entity in [1,2], Entity in [3,4])
        """
        return Or(self, other)

    def __invert__(self) -> QueryComponent:
        """
        Negates the query component

        Note: The return type is QueryComponent instead of Not because cases like
        Not(Not(Entity("1"))) should return Entity("1")
        instead of Not(Not(Entity("1")))
        """
        return Not(self)

    def to_dict(self) -> dict:
        """Convert the query component to a dictionary"""
        return self.to_expression().model_dump(
            exclude_none=True, exclude_unset=True, mode="json"
        )

    @abstractmethod
    def to_expression(self) -> Expression:
        """Convert the query component to an Expression object"""

    @abstractmethod
    def make_copy(self) -> QueryComponent:
        """Make a deep copy of the query component"""


# -- Operators --


class And(BaseQueryComponent):
    def __init__(self, *args: QueryComponent):
        # Flatten by detecting Ands inside args
        flatten_args = []
        for arg in args:
            if isinstance(arg, And):
                flatten_args.extend(arg.items)
            else:
                flatten_args.append(arg)
        self.items = flatten_args

    def __and__(self, other: QueryComponent) -> QueryComponent:
        # Flatten A&(B&(C&D)) into &(A,B,C,D)
        if isinstance(other, And):
            items = [*self.items, *other.items]
        else:
            items = [*self.items, other]
        # We first want to group the items by their class to make use of the
        # all operation
        items_by_class = {}
        for item in items:
            items_by_class.setdefault(item.__class__, []).append(item)
        # Now we can merge the items that are of the same class
        items_sorted = []
        for item_list in items_by_class.values():
            for item in item_list:
                items_sorted.append(item)
        # If there were in order, don't do this again, just AND them
        if items_sorted == items:
            return And(*items_sorted)
        # Otherwise, try to start from scratch, with the sorted items
        return all_(items_sorted)

    def to_expression(self) -> Expression:
        return Expression(
            type=ExpressionTypes.AND,
            value=[item.to_expression() for item in self.items],
        )

    def __repr__(self):
        items = [repr(item) for item in self.items]
        return f"And({', '.join(items)})"

    def make_copy(self) -> QueryComponent:
        """Make a deep copy of the query component"""
        items = [item.make_copy() for item in self.items]
        return And(*items)


class Or(BaseQueryComponent):
    def __init__(self, *args: QueryComponent):
        # Flatten by detecting Ors inside args
        flatten_args = []
        for arg in args:
            if isinstance(arg, Or):
                flatten_args.extend(arg.items)
            else:
                flatten_args.append(arg)
        self.items = flatten_args

    def __or__(self, other: QueryComponent) -> QueryComponent:
        # Flatten A|(B|(C|D)) into |(A,B,C,D)
        if isinstance(other, Or):
            items = [*self.items, *other.items]
        else:
            items = [*self.items, other]
        # We first want to group the items by their class to make use of the in operation
        items_by_class = {}
        for item in items:
            items_by_class.setdefault(item.__class__, []).append(item)
        # Now we can merge the items that are of the same class
        items_sorted = []
        for item_list in items_by_class.values():
            for item in item_list:
                items_sorted.append(item)
        # If there were in order, don't do this again, just OR them
        if items_sorted == items:
            return Or(*items_sorted)
        # Otherwise, try to start from scratch, with the sorted items
        return any_(items_sorted)

    def to_expression(self) -> Expression:
        return Expression(
            type=ExpressionTypes.OR,
            value=[item.to_expression() for item in self.items],
        )

    def __repr__(self):
        items = [repr(item) for item in self.items]
        return f"Or({', '.join(items)})"

    def make_copy(self) -> QueryComponent:
        """Make a deep copy of the query component"""
        items = [item.make_copy() for item in self.items]
        return Or(*items)


class Not(BaseQueryComponent):
    def __init__(self, item: QueryComponent):
        self.item = item

    def to_expression(self) -> Expression:
        return Expression(type=ExpressionTypes.NOT, value=self.item.to_expression())

    def __invert__(self) -> QueryComponent:
        return self.item

    def __repr__(self):
        return f"Not({repr(self.item)})"

    def make_copy(self) -> QueryComponent:
        """Make a deep copy of the query component"""
        return Not(self.item.make_copy())


def any_(items: list[QueryComponent]) -> QueryComponent:
    component = None
    if not items:
        raise ValueError("At least one item is required in any_")
    component = items[0]
    for item in items[1:]:
        component = component | item
    return component


def all_(items: list[QueryComponent]) -> QueryComponent:
    component = None
    if not items:
        raise ValueError("At least one item is required in all_")
    component = items[0]
    for item in items[1:]:
        component = component & item
    return component


# -- Filters --


class ListQueryComponent(BaseQueryComponent, ABC):
    """
    An abstract component that implements most of the duplicated logic of
    Entity, Keyword, Topic, Language, Source, etc
    All of these classes hold a list of items and have an operator (IN or ALL),
    so __and__ and __or__ with other objects of the same type can return a single
    object with the items joined.
    """

    def __init__(
        self, *items: str, operation: ExpressionOperation = ExpressionOperation.IN
    ):
        self.items = items
        self.operation = operation

    @abstractmethod
    def get_expression_type(self) -> ExpressionTypes:
        """Should return the type, like _entity_ or _rp_topic_"""

    def to_expression(self) -> Expression:
        return Expression(
            type=self.get_expression_type(),
            operation=self.operation,
            value=list(self.items),
        )

    def __or__(self, other: QueryComponent) -> QueryComponent:
        """
        Or operator for Entity, Keyword, Topic, Language, Source, etc.

        Examples:

        Joining an entity with something else should return an OR
        >>> Entity("1") | Topic("t1")
        Or(Entity('1'), Topic('t1'))

        But joining multiple entities should use the "in" operator and return
        a single entity:
        >>> Entity("1") | Entity("2") | Entity("3")
        Entity('1', '2', '3')

        Even if the entities are not contiguous:
        >>> Entity("1") | Topic("t1") | Entity("2")
        Or(Entity('1', '2'), Topic('t1'))

        But not if the operations are different
        >>> Entity("1") | (Entity("2") & Entity("3"))
        Or(Entity('1'), Entity('2', '3', operation=ExpressionOperation.ALL))
        >>> (Entity("1") & Entity("2")) | Entity("3")
        Or(Entity('1', '2', operation=ExpressionOperation.ALL), Entity('3'))
        """
        cls = self.__class__
        default = Or(self, other)
        operation = ExpressionOperation.IN
        if not isinstance(other, cls):
            return default
        if len(other.items) > 1 and other.operation != operation:
            return default
        if len(self.items) > 1 and self.operation != operation:
            return default
        return cls(*self.items, *other.items, operation=operation)

    def __and__(self, other: QueryComponent) -> QueryComponent:
        """
        And operator for Entity, Keyword, Topic, Language, Source, etc.

        Examples:

        Joining an entity with something else should return an AND
        >>> Entity("1") & Topic("t1")
        And(Entity('1'), Topic('t1'))

        But joining multiple entities should use the "all" operator and return
        a single entity:
        >>> Entity("1") & Entity("2") & Entity("3")
        Entity('1', '2', '3', operation=ExpressionOperation.ALL)

        Even if the entities are not contiguous:
        >>> Entity("1") & Topic("t1") & Entity("2")
        And(Entity('1', '2', operation=ExpressionOperation.ALL), Topic('t1'))

        But not if the operations are different
        >>> Entity("1") & (Entity("2") | Entity("3"))
        And(Entity('1'), Entity('2', '3'))
        >>> (Entity("1") | Entity("2")) & Entity("3")
        And(Entity('1', '2'), Entity('3'))
        """
        cls = self.__class__
        default = And(self, other)
        operation = ExpressionOperation.ALL
        if not isinstance(other, cls):
            return default
        if len(other.items) > 1 and other.operation != operation:
            return default
        if len(self.items) > 1 and self.operation != operation:
            return default
        return cls(*self.items, *other.items, operation=operation)

    def __repr__(self):
        items = [repr(item) for item in self.items]
        operation = ""
        if self.operation == ExpressionOperation.ALL:
            operation = ", operation=ExpressionOperation.ALL"
        class_name = self.__class__.__name__
        return f"{class_name}({', '.join(items)}{operation})"

    def make_copy(self) -> QueryComponent:
        """Make a deep copy of the query component"""
        cls = self.__class__
        return cls(*self.items, operation=self.operation)


class Entity(ListQueryComponent):
    def get_expression_type(self) -> ExpressionTypes:
        return ExpressionTypes.ENTITY


class Topic(ListQueryComponent):
    def get_expression_type(self) -> ExpressionTypes:
        return ExpressionTypes.TOPIC


class Keyword(ListQueryComponent):
    def __init__(
        self, *items: str, operation: ExpressionOperation = ExpressionOperation.IN
    ):
        super().__init__(*items, operation=operation)

    def get_expression_type(self) -> ExpressionTypes:
        return ExpressionTypes.KEYWORD

    def to_expression(self) -> Expression:
        items = [self._quote(item) for item in self.items]
        return Expression(
            type=self.get_expression_type(),
            operation=self.operation,
            value=list(items),
        )

    def _quote(self, item: str) -> str:
        if item[0] == '"' and item[-1] == '"':
            return item
        return f'"{item}"'


class Similarity(ListQueryComponent):
    def __init__(
        self, *items: str, operation: ExpressionOperation = ExpressionOperation.ALL
    ):
        if operation == ExpressionOperation.IN:
            raise ValueError("Similarity does not support `|` (OR) operator")
        super().__init__(*items, operation=operation)

    def get_expression_type(self) -> ExpressionTypes:
        return ExpressionTypes.SIMILARITY

    def __repr__(self):
        items = [repr(item) for item in self.items]
        operation = ""
        # This can't happen, the operation is always ALL, so no need to show it
        # if self.operation == ExpressionOperation.IN:
        #     operation = ", operation=ExpressionOperation.IN"
        class_name = self.__class__.__name__
        return f"{class_name}({', '.join(items)}{operation})"


class Language(ListQueryComponent):
    def get_expression_type(self) -> ExpressionTypes:
        return ExpressionTypes.LANGUAGE

    # Predefined languages

    @classmethod
    @property
    def arabic(cls):
        return Language("AR")

    @classmethod
    @property
    def chinese_traditional(cls):
        return Language("ZHTW")

    @classmethod
    @property
    def chinese_simplified(cls):
        return Language("ZHCN")

    @classmethod
    @property
    def dutch(cls):
        return Language("NL")

    @classmethod
    @property
    def english(cls):
        return Language("EN")

    @classmethod
    @property
    def french(cls):
        return Language("FR")

    @classmethod
    @property
    def german(cls):
        return Language("DE")

    @classmethod
    @property
    def italian(cls):
        return Language("IT")

    @classmethod
    @property
    def japanese(cls):
        return Language("JA")

    @classmethod
    @property
    def korean(cls):
        return Language("KO")

    @classmethod
    @property
    def portuguese(cls):
        return Language("PT")

    @classmethod
    @property
    def russian(cls):
        return Language("RU")

    @classmethod
    @property
    def spanish(cls):
        return Language("ES")


class Source(ListQueryComponent):
    def get_expression_type(self) -> ExpressionTypes:
        return ExpressionTypes.SOURCE


# Watchlist is a special case, as it's not a list of items


class Watchlist(BaseQueryComponent):
    def __init__(self, watchlist_id: str):
        self.watchlist_id = watchlist_id

    def to_expression(self) -> Expression:
        return Expression(
            type=ExpressionTypes.WATCHLIST,
            operation=ExpressionOperation.IN,
            value=self.watchlist_id,
        )

    def __repr__(self):
        return f"Watchlist({repr(self.watchlist_id)})"

    def make_copy(self) -> QueryComponent:
        """Make a deep copy of the query component"""
        return Watchlist(watchlist_id=self.watchlist_id)


class AbsoluteDateRangeQuery(BaseQueryComponent):
    def __init__(self, start: str, end: str):
        self.start = start
        self.end = end

    def to_expression(self) -> Expression:
        return Expression(
            type=ExpressionTypes.DATE,
            value=[self.start, self.end],
        )

    def make_copy(self) -> QueryComponent:
        """Make a deep copy of the query component"""
        return AbsoluteDateRangeQuery(start=self.start, end=self.end)


class RollingDateRangeQuery(BaseQueryComponent):
    """Used by the real RollingDateRange. Do not use this class directly"""

    def __init__(self, value: str):
        self.value = value

    def to_expression(self) -> Expression:
        return Expression(
            type=ExpressionTypes.DATE,
            value=self.value,
        )

    def make_copy(self) -> QueryComponent:
        """Make a deep copy of the query component"""
        return RollingDateRangeQuery(value=self.value)


class ContentType(ListQueryComponent):
    def get_expression_type(self) -> ExpressionTypes:
        return ExpressionTypes.CONTENT_TYPE

    @classmethod
    @property
    def pdf(cls):
        return ContentType("pdf")

    @classmethod
    @property
    def docx(cls):
        return ContentType("docx")

    @classmethod
    @property
    def pptx(cls):
        return ContentType("pptx")

    @classmethod
    @property
    def html(cls):
        return ContentType("html")

    @classmethod
    @property
    def txt(cls):
        return ContentType("txt")

    @classmethod
    @property
    def xlsx(cls):
        return ContentType("xlsx")

    @classmethod
    @property
    def csv(cls):
        return ContentType("csv")

    @classmethod
    @property
    def json(cls):
        return ContentType("json")

    @classmethod
    @property
    def xml(cls):
        return ContentType("xml")

    @classmethod
    @property
    def rtf(cls):
        return ContentType("rtf")

    @classmethod
    @property
    def md(cls):
        return ContentType("md")


class SentimentMetaclass(ABCMeta, type):
    """Only needed for blackmagic"""

    def __hash__(self):
        # Just blackmagic to make isinstance work
        return hash(self.__module__ + self.__name__)

    def __gt__(cls, value: Union[float, int]):
        return cls(value, operation=ExpressionOperation.GREATER_THAN)

    def __lt__(cls, value: Union[float, int]):
        return cls(value, operation=ExpressionOperation.LOWER_THAN)

    def __ge__(cls, value: Union[float, int]):
        _ = value
        raise ValueError("Sentiment only supports > and <, not >=")

    def __le__(cls, value: Union[float, int]):
        _ = value
        raise ValueError("Sentiment only supports > and <, not <=")

    def __eq__(cls, value: Union[float, int]):
        _ = value
        if isinstance(value, (float, int)):
            raise ValueError("Sentiment only supports > and <, not ==")
        else:
            # equal operator can be called by isinstance
            return super(cls).__eq__(value)

    def __ne__(cls, value: float):
        _ = value
        if isinstance(value, (float, int)):
            raise ValueError("Sentiment only supports > and <, not !=")
        else:
            # equal operator can be called by isinstance
            return super(cls).__eq__(value)


class Sentiment(BaseQueryComponent, metaclass=SentimentMetaclass):
    __metaclass__ = SentimentMetaclass

    def __init__(
        self,
        value: float,
        operation: ExpressionOperation = ExpressionOperation.GREATER_THAN,
    ):
        self.value = value
        self.operation = operation

    def to_expression(self) -> Expression:
        return Expression(
            type=ExpressionTypes.SENTIMENT,
            value=self.value,
            operation=self.operation,
        )

    def __repr__(self):
        return f"Sentiment(value={repr(self.value)}, operation={repr(self.operation)})"

    def make_copy(self) -> QueryComponent:
        """Make a deep copy of the query component"""
        return Sentiment(value=self.value, operation=self.operation)


def _expression_to_query_component(expression: Expression) -> QueryComponent:
    """
    Convert an Expression object to a QueryComponent object
    """
    if expression.type == ExpressionTypes.AND:
        return And(*[_expression_to_query_component(e) for e in expression.value])
    if expression.type == ExpressionTypes.OR:
        return Or(*[_expression_to_query_component(e) for e in expression.value])
    if expression.type == ExpressionTypes.NOT:
        return Not(_expression_to_query_component(expression.value))
    if expression.type == ExpressionTypes.ENTITY:
        return Entity(*expression.value, operation=expression.operation)
    if expression.type == ExpressionTypes.TOPIC:
        return Topic(*expression.value, operation=expression.operation)
    if expression.type == ExpressionTypes.KEYWORD:
        return Keyword(*expression.value, operation=expression.operation)
    if expression.type == ExpressionTypes.SIMILARITY:
        return Similarity(*expression.value, operation=expression.operation)
    if expression.type == ExpressionTypes.LANGUAGE:
        return Language(*expression.value, operation=expression.operation)
    if expression.type == ExpressionTypes.SOURCE:
        return Source(*expression.value, operation=expression.operation)
    if expression.type == ExpressionTypes.WATCHLIST:
        return Watchlist(expression.value)
    if expression.type == ExpressionTypes.DATE:
        if isinstance(expression.value, list):
            return AbsoluteDateRangeQuery(*expression.value)
        return RollingDateRangeQuery(expression.value)
    if expression.type == ExpressionTypes.CONTENT_TYPE:
        return ContentType(*expression.value, operation=expression.operation)
    if expression.type == ExpressionTypes.SENTIMENT:
        return Sentiment(expression.value, operation=expression.operation)
