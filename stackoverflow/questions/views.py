from django.shortcuts import render
import urllib
import json

# Create your views here.
def forecast_view(request):
    if request.method == 'POST':
            city = request.POST['city']
            city_capitalized = city.capitalize()
            safe_string_city = urllib.parse.quote_plus(city)
            
            #language = request.POST['language']
            #units = request.POST['units']

            #url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&lang='+language+'&appid=66d8dd58fe4ab3e2cbf275d5aee1d85b&units='+units).read()
            res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+safe_string_city+'&appid=66d8dd58fe4ab3e2cbf275d5aee1d85b').read()
            json_data = json.loads(res)

            data = {
                'country_code': json_data['sys']['country'],
                'coordinates': str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
                'weather': json_data['weather'][0]['main'],
                'description': json_data['weather'][0]['main'],
                'icon': 'http://openweathermap.org/img/wn/' + json_data['weather'][0]['icon'] + '@2x.png',

                'wind': json_data['wind']['speed'],
                'temperature': json_data['main']['temp'],
                'pressure': json_data['main']['pressure'],
                'humidity': json_data['main']['humidity'],
                'city': city_capitalized,
            }
    else:
        city = ''
        data = {}
    return render(request, 'weather/forecast.html', data)


def forecast_view2(request):
    if request.method == 'POST':
        if request.POST.get("filters"):
            pass
        elif request.POST.get("get_info"):
            city = request.POST['city']
            city_capitalized = city.capitalize()
            safe_string_city = urllib.parse.quote_plus(city)
            
            #language = request.POST['language']
            #units = request.POST['units']

            #url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&lang='+language+'&appid=66d8dd58fe4ab3e2cbf275d5aee1d85b&units='+units).read()
            res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+safe_string_city+'&appid=66d8dd58fe4ab3e2cbf275d5aee1d85b').read()
            json_data = json.loads(res)

            data = {
                'country_code': json_data['sys']['country'],
                'coordinates': str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
                'weather': json_data['weather'][0]['main'],
                'description': json_data['weather'][0]['main'],
                'icon': 'http://openweathermap.org/img/wn/' + json_data['weather'][0]['icon'] + '@2x.png',

                'wind': json_data['wind']['speed'],
                'temperature': json_data['main']['temp'],
                'pressure': json_data['main']['pressure'],
                'humidity': json_data['main']['humidity'],
                'city': city_capitalized,
            }
    else:
        city = ''
    return render(request, 'weather/forecast.html', data) 

    