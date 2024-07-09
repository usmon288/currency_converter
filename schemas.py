from pydantic import BaseModel
from typing import Dict

class ConversionRequest(BaseModel):
    amount: float

class ConversionResponse(BaseModel):
    conversions: Dict[str, float]
