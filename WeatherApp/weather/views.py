import requests
from django.shortcuts import render


# Create your views here.
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=d07e68bcb014a06a4d7b091c1456e711"

city = "Seattle"
res = requests.get(url.format(city))
print(res.text)


def index(request):
    return render(request, 'weather/index.html')
