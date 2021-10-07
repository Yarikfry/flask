# flask
# Додумался до этого, но ничего не дало
import requests

from flask import Flask, request

app = Flask(__name__)

APPID = "969511fc8e7d7f29b4b66ff1417a221e"  # <-- Put your OpenWeatherMap appid here!
URL_BASE = "http://api.openweathermap.org/data/2.5/"


@app.route('/')
def get_ip():
    name = request.args.get('name')
    ip = request.environ['HTTP_X_FORWARDED_FOR']
    r = requests.get(f'http://ip-api.com/json/{ip}')
    a = r.json()
    b = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={a["city"]}&appid={APPID}&units=metric&name={name}')
    return b.json()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
