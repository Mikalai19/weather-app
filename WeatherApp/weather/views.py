import requests
from django.shortcuts import render


# Create your views here.
url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=Fahrenheit&appid=d07e68bcb014a06a4d7b091c1456e711"

city = "Seattle"
res = requests.get(url.format(city)).json()

city_info = {
    'city': city,
    'temp': res['main']['temp'],
    'icon': res['weather']['icon'],
    'humidity': res['main']['humidity'],
    'wind': res['wind']['speed'],

}


def index(request):
    return render(request, 'weather/index.html')
