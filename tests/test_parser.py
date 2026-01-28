from weather_app.weather_parser import c_to_f, parse_current, parse_forecast

def test_celsius_to_fahrenheit():
    assert c_to_f(0) == 32.0
    assert c_to_f(100) == 212.0

def test_parse_current_weather():
    sample_data = {
        "name": "London",
        "sys": {"country": "GB", "sunrise": 1706170000, "sunset": 1706200000},
        "main": {"temp": 10, "feels_like": 8, "humidity": 80},
        "wind": {"speed": 5},
        "weather": [{"description": "clear sky", "main": "Clear"}]
    }

    result = parse_current(sample_data, "C")
    assert result["city"] == "London"
    assert result["temp"] == 10
    assert result["humidity"] == 80

def test_parse_forecast():
    sample_forecast = {
        "list": [
            {"dt_txt": "2024-01-25 12:00:00", "main": {"temp": 10}},
            {"dt_txt": "2024-01-25 18:00:00", "main": {"temp": 7}},
            {"dt_txt": "2024-01-26 12:00:00", "main": {"temp": 12}},
        ]
    }

    forecast = parse_forecast(sample_forecast, "C")
    assert len(forecast) >= 1
    assert "min" in forecast[0]
    assert "max" in forecast[0]
