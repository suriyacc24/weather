from django.shortcuts import render
import requests
from .models import Weather

# Replace with your OpenWeatherMap API key
API_KEY = '2d9c02b0ef95ba14af4fc0babcd2bf80'


def weather_view(request):
    # This view is used to display current weather data fetched from the API
    city = request.GET.get('city', 'London')  # Default city if no city is provided
    weather_data = None  # Initialize weather data as None

    if city:
        # Construct the URL for the OpenWeatherMap API call
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            # If the response is successful, parse the JSON data
            weather_data = response.json()

            # Create a new Weather record and save it to the database
            weather_record = Weather(
                city=weather_data.get('name'),
                temperature=weather_data['main'].get('temp'),
                condition=weather_data['weather'][0].get('description'),
                humidity=weather_data['main'].get('humidity'),
                wind_speed=weather_data['wind'].get('speed')
            )
            weather_record.save()

    # Render the weather data to the 'weather_app/index.html' template
    return render(request, 'weather_app/index.html', {'weather_data': weather_data})
