import requests
import logging
from datetime import datetime, timezone
from config import API_KEY

def get_weather(city):
    """
    Fetches the current weather for a given city using the OpenWeatherMap API.
    
    Args:
        city (str): Name of the city to retrieve weather information for.
    
    Returns:
        dict: Weather information including city name, temperature, humidity, 
              condition, wind speed, weather icon URL, and timestamp.
        None: If the API request fails.
    """
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"].title(),
            "wind_speed": data["wind"]["speed"],
            "icon": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png",
            "time": datetime.fromtimestamp(data["dt"], timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        }
        return weather_info
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return None
    


BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_weekly_forecast(city):
    """
    Fetches the weekly weather forecast for a given city using the OpenWeatherMap API.
    
    Args:
        city (str): Name of the city to retrieve the forecast for.
    
    Returns:
        list: A list of dictionaries containing daily forecast dates and temperatures.
        None: If the API request fails.
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if response.status_code == 200:
        forecast = []
        seen_dates = set()
        for entry in data["list"]:
            date = entry["dt_txt"].split(" ")[0]  
            if date not in seen_dates:
                seen_dates.add(date)
                forecast.append({
                    "date": date,
                    "temperature": entry["main"]["temp"]
                })
        return forecast
    else:
        return None
