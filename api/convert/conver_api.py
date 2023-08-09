import requests


from main import app

# получить курс ЦБ и нашего сервиса


@app.get('/api/get-currency')
async def currency_rate():
    # получаем апи цб
    cb_api = requests.get('https://cbu.uz/ru/arkhiv-kursov-valyut/json/').json()
    # получаем курс определенных валют
    usd_rate = cb_api[0]['Rate']
    eur_rate = cb_api[1]['Rate']
    rub_rate = cb_api[2]['Rate']
    return {'status': 1, 'rates': {'USD': usd_rate,
                                   'EUR': eur_rate,
                                   'RUB': rub_rate}}
