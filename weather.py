import requests

api_key = "99d14f14a9f8559015758e2599d89980"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print("\n🌍 City:", data["name"])
    print("🌡 Temperature:", data["main"]["temp"], "°C")
    print("☁ Weather:", data["weather"][0]["description"])
    print("💧 Humidity:", data["main"]["humidity"], "%")
    print("🌬 Wind Speed:", data["wind"]["speed"], "m/s")
else:
    print("\n❌ Error:", data.get("message"))