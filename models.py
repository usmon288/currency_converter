from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ConversionRecord(BaseModel):
    date_time: datetime
    amount: float
    conversions: dict
