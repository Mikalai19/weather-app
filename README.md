### Weather-app

This is a simple web site is design to search for weather in any city in the world.

### User story

Who:
As a visitor of web site:

What:

1. Once I landed on main page i want to see 4 cities' weather by default.
2. I want to type a city where I want to know the weather.
3. I want to see the weather of the city that i'm looking for.
4. I want to see other information such as humidity, wind and etc.
5. I want to see see hourly weather of the city i'm looking for

## Wire frame

![](WeatherApp/weather/templates/img/Screen%20Shot%202022-01-30%20at%209.54.51%20PM.png)

## Code Snippets

### Create a Model

```javascript

class City(models.Model):
    name = models.CharField(max_length=50)

    def __srt__(self):
        return self.name

```

### POST Form

```javascript

if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
```

### Parcing API data

```javascript

cities = City.objects.all()
    all_cities = []
    for city in cities:
     res = requests.get(url.format(city.name)).json()
    city_info = {
        'city': city.name,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon'],
        'humidity': res['main']['humidity'],
        'wind': res['wind']['speed'],

    }

    all_cities.append(city_info)

```

### API Resource

https://openweathermap.org
