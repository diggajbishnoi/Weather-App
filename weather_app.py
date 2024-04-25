# -*- coding: utf-8 -*-
"""Weather App.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tRciZ9L8OLXj1HTxIY6-J7-jC_CIcnqL

### Python Programming for Weather App:-
"""

import requests

api_key = '30d4741c779ba94c470ca1f63045390a'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}ºF")

