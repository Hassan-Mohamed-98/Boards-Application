from django.shortcuts import render
from .models import City
from .forms import CityForm
import requests

# Create your views here.
def get_weather_info(request):
    api_url = "http://api.openweathermap.org./data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
    # city_name = "Egypt"
    # url = api_url + city_name
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
    form = CityForm()
    cities = City.objects.all()
    weather_data = []
    city_weather = {}
    if cities:
        for city in cities:
            data_url = api_url + str(city)
            response = requests.get(data_url).json()
            city_weather = {
                'city': city,
                'description': response["weather"][0]["description"],
                'temperature': response["main"]["temp"],
                'icon': response["weather"][0]["icon"]
            }

    weather_data.append(city_weather)

    # weather_desc = result["weather"][0]["description"]
    # result["main"]["temp"]
    return render(request,'weather.html',{'weather data':weather_data, 'form':form})