from fastapi import Body
from main import app
from . profile_models import UserDent, CardDent
from database.profile_service import login_db, add_card,get_user_info

# регистрация пользователя
@app.post('/api/register_user')
async def user_registration(User_data: UserDent):
    print(User_data)
    # после регистрации выдать id пользователя
    return {'starus': 1, 'message': 'Registration complete'}

# вход в аккаунт
@app.post('/api/login_user')
async def login_user(phone_number: int = Body(), password: str = Body()):
    # проверка данных
    checker = login_db(phone_number, password)
    if checker:
        return {'status': 1, 'message': 'log in successfully'}
    return {'status': 0, 'message': 'login failed'}

@app.post('/api/add-card')
async def add_user_card(card_data: CardDent):
    # вызов функии для добавлении карты в бд
    result = add_card(card_data.card_number, card_data.user_id,
                      card_data.card_name, card_data.card_balance, card_data.exp_date)
    print(result)
    if result:
        # если успешно добавлена карта то статус 1\
        return {'status': 1, 'message': result}
    return {'status': 0, 'message': 'Card adeded'}

#  вывод даных о пользователе
@app.get('/api/user_data')
async def get_user_data(user_id: int):
    user_info = get_user_info(user_id)
    if user_info:
        return {'status': 1, 'message': user_info}
    return {'status': 0, 'message': 'IDI NA XUY'}


# Вывод всех карт пользователя
@app.get('/api/user-cards')
async def get_all_user_card(user_id):
    pass
