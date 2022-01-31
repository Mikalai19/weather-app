import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    # Create your views here.
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d07e68bcb014a06a4d7b091c1456e711"

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()  # take all data from table
    all_cities = []

    for city in cities:  # iterate all data from the table

        # get data for each city
        res = requests.get(url.format(city.name)).json()
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
# handed list of cities as param all_info

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)


def second(request):
    url = "http://pro.openweathermap.org/data/2.5/forecast/hourly?q={}&units=imperial&appid=d07e68bcb014a06a4d7b091c1456e711"

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()  # take all data from table
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()

        city_info = {
            'city': city.name,
            # 'time': res['sys']['dt_txt'],
            # 'icon': res['weather'][0]['icon'],
            # 'humidity': res['main']['humidity'],
            # 'wind': res['wind']['speed'],

        }
    all_cities.append(city_info)

    context = {'all_info': city_info, 'form': form}

    return render(request, 'second.html', context)


def third(request):

    return render(request, 'third.html')


def login(request):

    return render(request, 'login.html')
