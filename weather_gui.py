import tkinter as tk
import requests

# ---------------- WEATHER FUNCTION ---------------- #
def get_weather():
    city = city_entry.get()

    if city == "":
        result_label.config(text="⚠️ Please enter a city name!")
        return

    status_label.config(text="⏳ Fetching weather...")

    try:
        api_key = "99d14f14a9f8559015758e2599d89980"  
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            result_label.config(text="❌ City not found!")
            return

        weather = data["weather"][0]["main"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        # 🌈 Weather emoji mapping
        if weather == "Clear":
            icon = "☀️"
        elif weather == "Clouds":
            icon = "☁️"
        elif weather == "Rain":
            icon = "🌧️"
        elif weather == "Thunderstorm":
            icon = "⛈️"
        elif weather == "Snow":
            icon = "❄️"
        else:
            icon = "🌤️"

        result_label.config(
            text=f"{icon} Weather in {city}\n\n"
                 f"🌡️ Temperature: {temp}°C\n"
                 f"💧 Humidity: {humidity}%\n"
                 f"🌬️ Wind Speed: {wind} km/h"
        )

        status_label.config(text="✅ Done!")

    except:
        result_label.config(text="❌ Error fetching data!")
        status_label.config(text="")

# ---------------- UI SETUP ---------------- #
root = tk.Tk()
root.title("🌦️ Weather App")
root.geometry("400x450")
root.configure(bg="#1e1e2f")

# Center window
root.eval('tk::PlaceWindow . center')

# ---------------- TITLE ---------------- #
title = tk.Label(
    root,
    text="🌤️ My Weather App",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#1e1e2f"
)
title.pack(pady=15)

# ---------------- INPUT ---------------- #
city_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=25,
    justify="center"
)
city_entry.pack(pady=10)

# ---------------- BUTTON ---------------- #
button = tk.Button(
    root,
    text="🔍 Get Weather",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5,
    borderwidth=0,
    command=get_weather
)
button.pack(pady=10)

# ---------------- STATUS ---------------- #
status_label = tk.Label(
    root,
    text="",
    font=("Arial", 10),
    fg="lightgray",
    bg="#1e1e2f"
)
status_label.pack(pady=5)

# ---------------- RESULT CARD ---------------- #
result_label = tk.Label(
    root,
    text="📍 Enter a city to get weather",
    font=("Arial", 12),
    fg="white",
    bg="#2c2c3e",
    justify="left",
    padx=15,
    pady=15
)
result_label.pack(pady=20)

# ---------------- RUN ---------------- #
root.mainloop()