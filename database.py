from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from pymongo.database import Database

class DatabaseManager:
    def __init__(self, db_url: str, db_name: str):
        self.client = AsyncIOMotorClient(db_url)
        self.db: Database = self.client[db_name]

db_manager = DatabaseManager("mongodb://localhost:27017", "currency_db")
