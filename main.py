import os
import time

from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

from config.config import config as conf

os.environ["OPENAI_API_KEY"] = conf.config["open-ai"]["api-key"]

from src.database.db import init_db
from src.document.documents import Conversation, Query
from src.open_ai.open_ai_client import OpenAIClient

app = FastAPI()
open_ai_client = OpenAIClient()


@app.on_event("startup")
async def start_db():
    await init_db()


@app.get("/")
def read_root():
    return {"Hello": "World"}


class Request(BaseModel):
    message: str
    conversation_id: str


@app.post("/queries")
async def queries(request: Request):
    try:
        stream = open_ai_client.ask(request.message)
        conversation = await Conversation.get(request.conversation_id)

        if conversation is None:
            conversation = Conversation(context=request.message, initiated_by="user", initiated_at=int(time.time()),
                                        queries=[])

        query = Query(query=request.message, initiated_at=int(time.time()), response=None, responded_at=None)
        response_str = ""

        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                response_str += chunk.choices[0].delta.content

        query.response = response_str
        query.responded_at = int(time.time())
        conversation.queries.append(query)

        return await conversation.save()

    except HTTPException as e:
        raise HTTPException(status_code=402, detail=str(e))


@app.get("/conversations")
async def conversations():
    return await Conversation.find().to_list()


@app.get("/conversations/{conversation_id}")
async def conversations(conversation_id: str):
    return await Conversation.get(conversation_id)


@app.delete("/conversations/{conversation_id}")
async def delete_conversation(conversation_id: str):
    conversation = await Conversation.get(conversation_id)
    if conversation is None:
        raise HTTPException(status_code=404, detail="Conversation not found")
    await conversation.delete()

    return {"message": "Conversation deleted"}


@app.put("/conversations/{conversation_id}")
async def update_conversation(conversation_id: str, conversation: Conversation):
    conversation_db = await Conversation.get(conversation_id)
    if conversation_db is None:
        raise HTTPException(status_code=404, detail="Conversation not found")
    conversation_db.context = conversation.context
    conversation_db.initiated_by = conversation.initiated_by
    conversation_db.initiated_at = conversation.initiated_at
    conversation_db.queries = conversation.queries
    await conversation_db.save()

    return conversation_db
