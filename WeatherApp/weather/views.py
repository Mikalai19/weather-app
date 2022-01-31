import requests
from django.shortcuts import render
from .models import City


# Create your views here.
url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d07e68bcb014a06a4d7b091c1456e711"


cities = City.objects.all()  # take all data from table
all_cities = []

for city in cities:  # iterate all data from the table

    res = requests.get(url.format(city.name)).json()  # get data for each city
    # print('City ----->', res)
    city_info = {
        'city': city.name,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon'],
        'humidity': res['main']['humidity'],
        'wind': res['wind']['speed'],

    }

    # print('City ----->', city_info['city'])

    all_cities.append(city_info)  # insert those data

# humidity_info = res['main']['humidity']
# wind_info = res['wind']['speed']
# print(humidity_info)
# print(wind_info)
context = {'all_info': city_info}  # handed list of cities as param all_info


def index(request):
    return render(request, 'weather/index.html', context)
