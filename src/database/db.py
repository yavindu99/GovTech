from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from config.config import config as conf
from src.document.documents import Conversation


async def init_db():
    username = conf.config['mongodb']['username']
    password = conf.config['mongodb']['password']
    db_name = conf.config['mongodb']['name']

    # Create Motor client
    client = AsyncIOMotorClient(f"mongodb://{username}:{password}@localhost:27017")

    # Init beanie with the Product document class
    await init_beanie(database=client[f"{db_name}"], document_models=[Conversation])
