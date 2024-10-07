from typing import Optional

from beanie import Document
from pydantic import BaseModel


# To hold context of the conversation


class Query(BaseModel):
    query: str
    # initiated timestamp
    initiated_at: int
    response: Optional[str] = None
    # respond timestamp
    responded_at: Optional[int] = None


class Conversation(Document):
    context: str
    initiated_by: str
    initiated_at: int
    queries: list[Query]

    class Settings:
        name = "conversations"  # Collection name
