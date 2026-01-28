from datetime import datetime
from collections import defaultdict

def c_to_f(temp):
    return round((temp * 9 / 5) + 32, 1)

def parse_current(data, unit="C"):
    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]

    if unit == "F":
        temp = c_to_f(temp)
        feels = c_to_f(feels)

    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temp": temp,
        "feels": feels,
        "humidity": data["main"]["humidity"],
        "wind": data["wind"]["speed"],
        "desc": data["weather"][0]["description"].title(),
        "icon": data["weather"][0]["main"],
        "sunrise": datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M"),
        "sunset": datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M"),
        "updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def parse_forecast(data, unit="C"):
    days = defaultdict(list)

    for item in data["list"]:
        date = item["dt_txt"].split()[0]
        temp = item["main"]["temp"]
        if unit == "F":
            temp = c_to_f(temp)
        days[date].append(temp)

    result = []
    for day, temps in list(days.items())[:5]:
        result.append({
            "date": day,
            "min": round(min(temps), 1),
            "max": round(max(temps), 1)
        })

    return result

