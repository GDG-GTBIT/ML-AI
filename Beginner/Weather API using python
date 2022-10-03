import datetime as dt
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "4c715a017242fcc01ab48bff476e2c2e"
CITY = input("Enter the city ")

def kelvin_to_celsius_farenheit(kelvin):
    celsius= kelvin-273.15
    farenheit=celsius*(9/5)+32
    return celsius,farenheit


url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

temp_kelvin=response['main'] ['temp']
temp_celsius, temp_farenheit= kelvin_to_celsius_farenheit(temp_kelvin)
feels_like_kelvin=response['main'] ['feels_like']
feels_like_celsius, feels_like_farenheit= kelvin_to_celsius_farenheit(feels_like_kelvin)
wind_speed = response ['wind']['speed']
humidity = response ['main']['humidity']
description = response ['weather'][0]['description']
sunrise_time= dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time= dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"Temperature in {CITY} : {temp_celsius:.2f}°C or {temp_farenheit:.2f}°F ")
print(f"Temperature in {CITY} : feels like {feels_like_celsius:.2f}°C or {feels_like_farenheit:.2f}°F ")
print(f"Humidity in {CITY} : {humidity}% ")
print(f"Wind speed in {CITY} : {wind_speed}m/s ")
print(f"General weather in {CITY} : {description}")
print(f"Sun rises in {CITY} at {sunrise_time} local time.")
print(f"Sun sets in {CITY} at {sunset_time} local time.")

