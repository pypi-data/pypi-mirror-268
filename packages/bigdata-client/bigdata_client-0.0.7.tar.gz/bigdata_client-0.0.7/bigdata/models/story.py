from dataclasses import dataclass
from enum import Enum

from bigdata.query_type import QueryType


@dataclass
class StorySource:
    """The source of a story"""

    key: str
    name: str
    rank: int


class StoryType(Enum):
    """
    The type of the story. A news, a transcript or an uploaded file.
    """

    NEWS = "news"
    TRANSCRIPTS = "transcripts"
    FILES = "files"


@dataclass
class StorySentenceEntity:
    """
    A detection instance of an entity in a sentence
    """

    key: str
    start: int
    end: int
    query_type: QueryType


@dataclass
class StorySentence:
    paragraph: int
    sentence: int


@dataclass
class StoryChunk:
    """
    A chunk of text representing a contextual unit within the document
    """

    text: str
    chunk: int
    entities: list[StorySentenceEntity]
    sentences: list[StorySentence]
