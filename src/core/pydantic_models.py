from pydantic import BaseModel, Field
from typing import List
from datetime import date


class PredictRequest(BaseModel):
    ticker: str = Field(..., example="AAPL", description="Тикер компании")
    days: int = Field(default=30, ge=1, le=365, description="Горизонт прогноза в днях")


class PredictionPoint(BaseModel):
    date: date
    value: float
    lower: float
    upper: float


class PredictResponse(BaseModel):
    ticker: str
    forecast: List[PredictionPoint]
