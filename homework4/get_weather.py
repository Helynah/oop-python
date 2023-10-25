# Hellen M Wanyana
# CSC-287-01
# This application will retrieve weather data from the service and dispaly a summary

"""Get weather module"""
import requests

from weather_parser import WeatherParser

WEATHER_URL = "https://wttr.in/Boston?format=j1"

print(f"\nGetting live data from {WEATHER_URL}.")
response = requests.get(WEATHER_URL, timeout=60)
weatherParser = WeatherParser(response.json())

print("Enter city: Boston")
print(f"Currently feels like: {weatherParser.get_feels_like_f()} degrees F")
print(f"Current weather is: {weatherParser.get_weather_description()}")
print(f"Cloud Cover: {weatherParser.get_cloud_cover()}%")
print(f"Sunrise: {weatherParser.get_sunrise()}")
print(f"Sunset: {weatherParser.get_sunset()}")
