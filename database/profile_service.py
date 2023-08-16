from database.models import User, Card
from database import get_db
#регистрация


def login_db(phone_number, password):
    db = next(get_db())
    checker = db.query(User).filter_by(phone_number=phone_number, password=password)
    return checker


def add_card(card_number, user_id, exp_date, card_name, card_balance):
    db = next(get_db())
    add_card = Card(card_number=card_number, user_id=user_id,
                    card_name=card_name, card_balance=card_balance, exp_date=exp_date)
    db.add(add_card)
    db.commit()
    return add_card.id



def get_user_info(user_id):
    db = next(get_db())
    get_info = db.query(User).filter_by(id=user_id).first()
    return get_info