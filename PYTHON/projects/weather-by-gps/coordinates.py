# importing geopy library
from geopy.geocoders import Nominatim

from exceptions import CantGetCoordinates
from config import USE_ROUNDED_COORDS

# there is a problem when gps function returns "tuple[float, float]"
# what is latitude and what is longitude in that tuple? Not clear.
# so, we'll be using "NamedTuple"
from typing import NamedTuple
class Coordinates(NamedTuple):
    latitude: float
    longitude: float

# def get_gps_coordinates(location_name: str = "Gosainganj Lucknow") -> tuple[float, float]:
def get_coordinates(location_name: str = "Gosainganj Lucknow") \
        -> Coordinates:
# calling the Nominatim tool
    loc = Nominatim(user_agent="GetLoc")
     
    # entering the location name
    getLoc = loc.geocode(location_name)
    print("type:", type(getLoc))

    # check if coords reseived correctly. (When not - getLoc = None)
    # raise custom exception
    if getLoc is None:
        raise CantGetCoordinates
    
    latitude = getLoc.latitude
    longitude = getLoc.longitude
    # round coords
    if USE_ROUNDED_COORDS:
        latitude, longitude = map(lambda c: round(c, 1), [latitude, longitude])

    # printing address
    # print(getLoc.address)
     
    # printing latitude and longitude
    # print("Latitude = ", getLoc.latitude, "\n")
    # print("Longitude = ", getLoc.longitude)
    return Coordinates(latitude=getLoc.latitude, longitude=getLoc.longitude)
# And unpacking also works
# lat, lon = get_gps_coordinates("Somewhere")
# Or
# coordinates = get_gps_coordinates("M")
# lat = coordinates.latitude

# SECOND variant of gps function
from typing import Literal
def _gps2() -> dict[Literal["latitude"] | Literal["longitude"], float]:
    return{"latitude": 10, "longitude": 20}
# coordinates = get_gps_coordinates("W")
# print( coordinates["latitude"])

# THIRD variant of gps function
from typing import TypedDict
class Coordinates3(TypedDict):
    latitude: float
    longitude: float
def _gps3() -> Coordinates3:
    return Coordinates3(**{"latitude": 10, "longitude": 20})

# FOURTH variant of gps function
# using dataclass
# the main difference between "dataclass" and "NamedTuple" is that
# Tuple variables cannot be modified
# BUT this dataclass uses 328 bytes & NAmedTuple - 104 bytes
from dataclasses import dataclass
@dataclass
class Coordinates4:
    latitude: float
    longitude: float
def _gps4() -> Coordinates4:
    return Coordinates4(**{"latitude": 10, "longitude": 20})


if __name__ == "__main__":
    get_coordinates()
