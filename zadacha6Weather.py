#Создайте программу, которая будет запрашивать данные о текущей погоде в
#заданном городе через открытый API и выводить их на экран.

import requests
import json

APIkey = "205f114eaf923c8a254f6d985fb522ae"
cituName = 'Липецк'

api_url = f'https://api.openweathermap.org/data/2.5/weather?q={cituName}&appid={APIkey}'
response = requests.get(api_url)

if response.status_code == 200:
    data = json.load(response.text)
    print(data)
else:
    print("Ошибка при выполнении запроса:", response.status_code)