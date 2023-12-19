import requests
import json

def get_api_key():
    with open('./config.json') as config_file:
        config = json.load(config_file)
        return config['API_KEY']

API_KEY = get_api_key()
def get_weather(city):
    try:
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${API_KEY}')
        weather_data = response.json()
        print(f'Clima em {city}:')
        print(f'Temperatura: {weather_data["main"]["temp"]}°C')
        print(f'Descrição: {weather_data["weather"][0]["description"]}')
    except requests.RequestException as e:
        print('Erro ao obter informações meteorológicas:', e)

get_weather('Rio de Janeiro')
