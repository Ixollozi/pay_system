from fastapi import Body
from main import app
from . profile_models import UserDent

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
    checker = None

    #если данные верны, отправляем юзер айди
    return {'starus': 1, 'message': 'login in'}

