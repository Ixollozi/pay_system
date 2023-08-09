from pydantic import BaseModel
from datetime import datetime
# Жан Пьер Польнареф


# модель ввода данных

class UserDent(BaseModel):
    name: str
    surname: str
    profile_photo: str
    email: str
    phone_number: int
    password: str
    city: str
    reg_date: datetime
    password: str
# Модель для карты пользователя


class CardDent(BaseModel):
    card_number: int
    cardholder: str
    exp_date: int
    card_balance: float
    card_name: str
