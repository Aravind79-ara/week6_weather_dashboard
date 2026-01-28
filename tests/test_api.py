from weather_app.weather_api import WeatherAPI

def test_weather_api_object_creation():
    api = WeatherAPI()
    assert api is not None

def test_cache_directory_exists():
    api = WeatherAPI()
    assert api.cache_dir.exists()
