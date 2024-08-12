import requests

API_KEY = "b17a54c89e7136e997b3f8e8a2df89b4"  # API KEY

def fetch_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] != 200:
            return None
        weather = {
            "temp": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
        return weather
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None
