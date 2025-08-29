import config
import requests

api_key = config.API_KEY
location = getattr(config, "LOCATION", "Stafford, UK")

url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

response = requests.get(url)

print(response.json())

data = response.json()

print(data["main"]["temp"])
print(data["main"]["humidity"])
print(data["main"]["pressure"])
print(data["main"]["temp_min"])
print(data["main"]["temp_max"])
print(data["main"]["feels_like"])
print(data["wind"]["speed"])
print(data["wind"]["deg"])
print(data["wind"]["gust"])
print(data["name"])
print(data["sys"]["country"])
print(data["weather"][0]["description"])
print(data["weather"][0]["icon"])
print(data["weather"][0]["id"])
print(data["weather"][0]["main"])
print(data["weather"][0]["icon"])
print(data["weather"][0]["id"])
print(data["weather"][0]["main"])