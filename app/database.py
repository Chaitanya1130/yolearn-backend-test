from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# Load .env file (if running locally)
load_dotenv()

mongo_uri = os.environ.get("mongo_uri")
db_name = os.environ.get("db_name")

if not mongo_uri:
    raise ValueError("MONGO_URI environment variable not set. Ensure it's defined in Railway variables or a .env file.")

if not db_name:
    raise ValueError("DB_NAME environment variable not set. Ensure it's defined in Railway variables or a .env file.")

client = AsyncIOMotorClient(mongo_uri)
db = client[db_name]

async def connect_db():
    global client
    if client is None:
        client = AsyncIOMotorClient(mongo_uri)

async def get_text_collection():
    await connect_db()
    return db["text_collection"]
