import requests
import json
print("weather Dashboard")
api_key = "b1e92488bad6ba62e38a22bee22caefe"
base_url = "http://api.openweathermap.org/data/2.5/weather"




while true:
    city_name = input("Enter the city name: ").strip()
    
    if city_name.lower() == "exit":
        break
    
    if not city_name:
        print("Please enter a valid city name.")
        continue 
    params = {
    "q": city_name,
    "appid": api_key,
    "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        country_name = data["sys"]["country"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        weather_description = data["weather"][0]["description"]
        print(f"The weather in {city_name}, {country_name} is {temperature}°C and {weather_description}.")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} km/h \n")


    except keyError:
        print("Invalid city name. Please try again.")

        

