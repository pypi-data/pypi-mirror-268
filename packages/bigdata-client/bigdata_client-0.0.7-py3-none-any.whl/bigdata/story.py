import datetime
from dataclasses import dataclass

from bigdata.api.search import ChunkedStoryResponse
from bigdata.models.story import (
    StoryChunk,
    StorySentence,
    StorySentenceEntity,
    StorySource,
    StoryType,
)


@dataclass
class Story:
    """A story object"""

    id: str
    headline: str
    sentiment: float
    story_type: StoryType
    source: StorySource
    timestamp: datetime.datetime
    chunks: list[StoryChunk]
    language: str

    @classmethod
    def from_response(cls, response: ChunkedStoryResponse) -> "Story":
        source = StorySource(
            key=response.source_key,
            name=response.source_name,
            rank=response.source_rank,
        )
        chunks = [
            StoryChunk(
                s.text,
                s.cnum,
                [
                    StorySentenceEntity(e.key, e.start, e.end, e.queryType)
                    for e in s.entities
                ],
                [StorySentence(e.pnum, e.snum) for e in s.sentences],
            )
            for s in response.chunks
        ]
        story = cls(
            id=response.id,
            headline=response.headline,
            sentiment=response.sentiment,
            story_type=response.story_type,
            source=source,
            timestamp=response.timestamp,
            chunks=chunks,
            language=response.language,
        )
        return story

    def __str__(self) -> str:
        """
        Returns a string representation of the story.
        """
        chunks_repr = "\n".join(f"* {chunk.text}" for chunk in self.chunks)
        return (
            f"Story ID:  {self.id}\n"
            f"Timestamp: {self.timestamp}\n"
            f"Doc type:  {self.story_type.value}\n"
            f"Source:    {self.source.name} ({self.source.rank})\n"
            f"Title:     {self.headline}\n"
            f"Language:  {self.language}\n"
            f"Sentiment: {self.sentiment}\n"
            f"Sentence matches:\n{chunks_repr}"
        )
