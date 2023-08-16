from main import app
from .transfers_models import P2PDent


# Запрос на перевод денег между картами
@app.post('/api/transfer-money')
async def money_transfer(transfer_data: P2PDent):
    result = transfer_data
    print(result)

    return {'status': 1, 'message': result}


# Функция получения последних транзакций
@app.get('/api/monitoring')
async def user_payments(user_id: int):
    pass