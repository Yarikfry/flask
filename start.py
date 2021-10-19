from pprint import pprint
import requests

from flask import Flask, request

app = Flask(__name__)

APPID = "969511fc8e7d7f29b4b66ff1417a221e"  # <-- Put your OpenWeatherMap appid here!
URL_BASE = "http://api.openweathermap.org/data/2.5/"  # ссылка из которой берем ip
URL_BASE4 = "http://pro.openweathermap.org/data/2.5/"

@app.route('/')  # начало Flask
def get_ip():  # функция
    ip = request.environ['HTTP_X_FORWARDED_FOR']   # запрос
    r = requests.get(f'http://ip-api.com/json/{ip}')  # запрос ip из ссылки погоды
    a = r.json()  # вводим для r формат json
    b = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={a["city"]}&appid={APPID}&units=metric')
    data = dict(city=b.json()['name'], weather=b.json()['main']['temp'], wind=b.json()['wind']['speed'])
    r4 = requests.get(f'http://pro.openweathermap.org/data/2.5/forecast')
    # a4 = r4.json()
    b4 = requests.get(f'http://pro.openweathermap.org/data/2.5/forecast/hourly?q={a["city"]}&appid={APPID}')
    data4 = dict(location=b4.json()['name'])
    pprint(b.json() and b4.json())
    return data and data4

if __name__ == '__main__':
    app.run(debug=True, port=5000)
