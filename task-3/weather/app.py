from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)
api_key = "b1e92488bad6ba62e38a22bee22caefe"
base_url = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.form.get("city").strip()
        url = base_url + "appid=" + api_key + "&q=" + city
        params = {   
        "q": city_name,
        "appid": api_key,
        "units": "metric"
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            print(data)
            weather_data = {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"],
                "wind_speed": data["wind"]["speed"],
                "icon": data["weather"][0]["icon"]
            }
        except:
            error_message = "Invalid city name or network error"

        return render_template("index.html", weather = weather_data, error = error_message)
if __name__ == "__main__":
    app.run(debug=True)
