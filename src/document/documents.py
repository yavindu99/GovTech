from typing import Optional

from beanie import Document, Link


# To hold context of the conversation
class Conversation(Document):
    context: str
    initiated_by: str
    initiated_at: int

    class Settings:
        name = "conversations"  # Collection name


class Query(Document):
    query: str
    # initiated timestamp
    initiated_at: int
    response: Optional[str]
    # respond timestamp
    responded_at: Optional[int]
    # link to the conversation
    conversation: Link[Conversation]

    class Settings:
        name = "queries"  # Collection name

