import requests
from django.shortcuts import render


# Create your views here.
url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d07e68bcb014a06a4d7b091c1456e711"

city = "Seattle"
res = requests.get(url.format(city)).json()

city_info = {
    'city': city,
    'temp': res['main']['temp'],
    'icon': res['weather'][0]['icon'],
    'humidity': res['main']['humidity'],
    'wind': res['wind']['speed'],

}
# humidity_info = res['main']['humidity']
# wind_info = res['wind']['speed']
# print(humidity_info)
# print(wind_info)
context = {'info': city_info}


def index(request):
    return render(request, 'weather/index.html', context)
