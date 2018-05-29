from django.shortcuts import render
import requests

def get_weather(url):
    result = requests.get(url)
    print(result.text)

if __name__ == '__main__':
    get_weather('http://api.openweathermap.org/data/2.5/weather?q=Moscow&APPID=852f1c54929b7c4465c270c676bad5d4')


