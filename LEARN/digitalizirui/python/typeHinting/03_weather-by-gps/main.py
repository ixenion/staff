#!/usr/bin/env python3.10
# ^ is shebang
# exec this to be able run this program like "$ weather"
# sudo ln -s $(pwd)/main.py /usr/local/bin/weather

from coordinates_refactored import get_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather
from exceptions import ApiServiceError, CantGetCoordinates

def main():
    try:
        coordinates = get_coordinates()
    except CantGetCoordinates:
        print("Cannot get GPS coordinates")
        exit(1)
    try:
        weather = get_weather(coordinates)
    except ApiServiceError:
        print(f"Cannot get weather data by coordinates {coordinates}")
        exit(1)
    print(format_weather(weather))


if __name__ == "__main__":
    main()




