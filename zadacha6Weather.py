#Создайте программу, которая будет запрашивать данные о текущей погоде в
#заданном городе через открытый API и выводить их на экран.

import requests
import json

cituName = input('Введите город (пример Липецк): ')

api_url = f'https://api.weatherapi.com/v1/current.json?key=f9041ec3e97e4629a9c124428231109&q={cituName}&aqi=no'
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    print(f'Было обнавлено - {data["current"]["last_updated"]}')
    print(f'{data["location"]["name"]}, {data["location"]["country"]}')
    print(f'Погода: {data["current"]["temp_c"]} градусов')
    print(f'Влажность {data["current"]["humidity"]}')
else:
    print("Ошибка при выполнении запроса:", response.status_code)