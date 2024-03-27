from datetime import datetime
from enum import Enum
import json
from json.decoder import JSONDecodeError
import ssl
from typing import Literal, NamedTuple
import urllib.request
from urllib.error import URLError

from coordinates import Coordinates
import config
from exceptions import ApiServiceError

Celsius = float

class WeatherType(Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморозь"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"
# print(WeatherType.RAIN.name)
# print(WeatherType.RAIN.value)

# Why use "Enum"?
def _print_weather_type(weather_type: WeatherType) -> None:
    print(weather_type.value)
# And with "Enum" we can pass NOT just "WeatherType" as described in constructor
# But "WeatherType.RAIN" and get its value
#_print_weather_type(WeatherType.RAIN)
# but without "Enum" inheritance it would be impossible
#print(isinstance(WeatherType.RAIN, WeatherType)) # True
# Iterations also possible
#for weather_type in WeatherType:
#    print(weather_type.name, weather_type.value)

class Weather(NamedTuple):
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str

def get_weather(coordinates: Coordinates) -> Weather:
    """Request weather in OperWeather API and returns it"""
    openweather_response = _get_openweather_response(
            longitude=coordinates.longitude,
            latitude=coordinates.latitude)
    weather = _parse_openweather_response(openweather_response)
    return weather

def _get_openweather_response(latitude: float, longitude: float) -> str:
    ssl._create_default_https_context = ssl._create_unverified_context
    url = config.OPENWEATHER_URL_TEMPLATE.format(
            latitude=latitude, longitude=longitude)
    try:
        return urllib.request.urlopen(url).read()
    except URLError:
        raise ApiServiceError

def _parse_openweather_response(openweather_response: str) -> Weather:
    try:
        openweather_dict = json.loads(openweather_response)
    except JSONDecodeError:
        raise ApiServiceError
    return Weather(
        temperature=_parse_temperature(openweather_dict),
        weather_type=_parse_weather_type(openweather_dict),
        sunrise=_parse_sun_time(openweather_dict, "sunrise"),
        sunset=_parse_sun_time(openweather_dict, "sunset"),
        city=config.LOCATION
            )

def _parse_temperature(openweather_dict: dict) -> Celsius:
    return round(openweather_dict["main"]["temp"])

def _parse_weather_type(openweather_dict: dict) -> WeatherType:
    try:
        weather_type_id = str(openweather_dict["weather"][0]["id"])
    except (IndexError, KeyError):
        raise ApiServiceError
    weather_types = {
            "1": WeatherType.THUNDERSTORM,
            "3": WeatherType.DRIZZLE,
            "5": WeatherType.RAIN,
            "6": WeatherType.SNOW,
            "7": WeatherType.FOG,
            "800": WeatherType.CLEAR,
            "80": WeatherType.CLOUDS
            }
    for _id, _weather_type in weather_types.items():
        if weather_type_id.startswith(_id):
            return _weather_type
    raise ApiServiceError

def _parse_sun_time(
        openweather_dict: dict,
        time: Literal["sunrise"] | Literal["sunset"]) -> datetime:
    return datetime.fromtimestamp(openweather_dict["sys"][time])

if __name__ == "__main__":
    print(get_weather(Coordinates(latitude=55.7, longitude=37.6)))
