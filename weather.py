import requests
import os
import dotenv

API_KEY = os.getenv("WEATHER_API_KEY")
if not API_KEY:
    raise ValueError("Missing WEATHER_API_KEY in environment variables.")

def get_weather(city_name):
    # Example using OpenWeatherMap API
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"Weather in {city_name}: {temp}°C, {description}")
    else:
        print(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)