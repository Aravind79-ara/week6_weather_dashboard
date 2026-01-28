from weather_app.weather_dispaly import show_current, show_forecast

def test_show_current(capsys):
    sample_weather = {
        "city": "Paris",
        "country": "FR",
        "temp": 15,
        "feels": 14,
        "desc": "Clear Sky",
        "icon": "Clear",
        "humidity": 60,
        "wind": 3,
        "sunrise": "06:30",
        "sunset": "18:45",
        "updated": "2024-01-25 10:00"
    }

    show_current(sample_weather)
    captured = capsys.readouterr()
    assert "Paris" in captured.out
    assert "Temperature" in captured.out

def test_show_forecast(capsys):
    forecast = [
        {"date": "2024-01-25", "min": 7, "max": 12},
        {"date": "2024-01-26", "min": 6, "max": 10}
    ]

    show_forecast(forecast)
    captured = capsys.readouterr()
    assert "2024-01-25" in captured.out
