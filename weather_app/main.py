from .weather_api import WeatherAPI
from .weather_parser import parse_current, parse_forecast
from .weather_dispaly import show_current, show_forecast
from .config import DEFAULT_UNIT

def main():
    api = WeatherAPI()
    unit = DEFAULT_UNIT

    while True:
        city = input("\nEnter city name (or 'quit'): ")
        if city.lower() == "quit":
            break

        current, cached1 = api.current_weather(city)
        forecast, cached2 = api.forecast(city)

        if not current or not forecast:
            continue

        current_data = parse_current(current, unit)
        forecast_data = parse_forecast(forecast, unit)

        show_current(current_data)
        show_forecast(forecast_data)

        if cached1 or cached2:
            print("\nℹ️ Using cached data")

if __name__ == "__main__":
    main()
