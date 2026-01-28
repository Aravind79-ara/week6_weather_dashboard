ICONS = {
    "Clear": "☀️",
    "Clouds": "☁️",
    "Rain": "🌧️",
    "Snow": "❄️",
    "Thunderstorm": "⛈️",
    "Drizzle": "🌦️",
    "Mist": "🌫️"
}

def show_current(w):
    print("\n🌤️ CURRENT WEATHER")
    print("**********************")
    print(f"📍 {w['city']}, {w['country']}")
    print(f"Temperature: {w['temp']}°")
    print(f"Feels Like:  {w['feels']}°")
    print(f"Condition:   {w['desc']} {ICONS.get(w['icon'], '')}")
    print(f"Humidity:    {w['humidity']}%")
    print(f"Wind:        {w['wind']} km/h")
    print(f"Sunrise:     {w['sunrise']}")
    print(f"Sunset:      {w['sunset']}")
    print(f"Updated:     {w['updated']}")

def show_forecast(forecast):
    print("\n📅 5-DAY FORECAST")
    print("*********************")
    for day in forecast:
        print(f"{day['date']}: {day['max']}° / {day['min']}°")
