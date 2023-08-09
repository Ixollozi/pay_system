from datetime import datetime
from pydantic import BaseModel

# модель перевода с карты на карту

class P2P2Dent(BaseModel):
    card_from: int
    amount: float
    card_to: int
    trasfer_date: datetime
