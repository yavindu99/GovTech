import time

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from src.document.documents import Conversation, Query


async def init_db():
    # Create Motor client
    client = AsyncIOMotorClient("mongodb://root:1234@localhost:27017")

    # Init beanie with the Product document class
    await init_beanie(database=client["gov_tech"], document_models=[Conversation, Query])

    conversion = Conversation(context="test", initiated_by="user", initiated_at=int(time.time()))
    await conversion.save()

    query = Query(query="test", initiated_at=int(time.time()), response=None, responded_at=None,
                  conversation=conversion)
    await query.save()
