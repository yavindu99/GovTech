import time

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from config.config import config as conf
from src.document.documents import Conversation, Query


async def init_db():
    username = conf.config['mongodb']['username']
    password = conf.config['mongodb']['password']
    db_name = conf.config['mongodb']['db_name']

    # Create Motor client
    client = AsyncIOMotorClient(f"mongodb://{username}:{password}@localhost:27017")

    # Init beanie with the Product document class
    await init_beanie(database=client[f"{db_name}"], document_models=[Conversation, Query])

    conversion = Conversation(context="test", initiated_by="user", initiated_at=int(time.time()))
    await conversion.save()

    query = Query(query="test", initiated_at=int(time.time()), response=None, responded_at=None,
                  conversation=conversion)
    await query.save()
