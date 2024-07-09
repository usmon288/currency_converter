from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from database import db_manager
from models import ConversionRecord
from schemas import ConversionRequest, ConversionResponse
from utils import get_exchange_rates, convert_currency

app = FastAPI()

@app.post("/convert", response_model=ConversionResponse)
async def convert_currency_endpoint(request: ConversionRequest):
    try:
        rates = get_exchange_rates()
        conversions = convert_currency(request.amount, rates)

        record = ConversionRecord(
            date_time=datetime.now(),
            amount=request.amount,
            conversions=conversions
        )

        result = await db_manager.db.conversions.insert_one(record.dict(by_alias=True))

        return ConversionResponse(conversions=conversions)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/history", response_model=List[ConversionRecord])
async def get_conversion_history():
    try:
        records = await db_manager.db.conversions.find().to_list(1000)
        return records
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))