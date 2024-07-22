from geopy.geocoders import Nominatim
from geopy.location import Location as GeopyLocation

from exceptions import CantGetCoordinates
from config import USE_ROUNDED_COORDS, LOCATION

from typing import NamedTuple
class Coordinates(NamedTuple):
    latitude: float
    longitude: float

def get_coordinates() -> Coordinates:
    """Returns current coordinates using geopy lib"""
    coordinates = _get_geopy_coordinates()
    return _round_coordinates(coordinates)

def _get_geopy_coordinates() -> Coordinates:
    geopy_output = _get_geopy_output(LOCATION)
    coordinates = _parse_coordinates(geopy_output)
    return coordinates

def _get_geopy_output(location: str = "Ufa") -> GeopyLocation:
    loc = Nominatim(user_agent="GetLoc")
    output = loc.geocode(location)
    if output is None:
        raise CantGetCoordinates
    return output

def _parse_coordinates(geopy_output: GeopyLocation) -> Coordinates:
    try:
        latitude = geopy_output.latitude
        longitude = geopy_output.longitude
    except AttributeError:
        raise CantGetCoordinates
    return Coordinates(
            latitude=latitude,
            longitude=longitude
            )
    
def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not USE_ROUNDED_COORDS:
        return coordinates
    return Coordinates(*map(
        lambda c: round(c, 1),
        [coordinates.latitude, coordinates.longitude]
        ))

    


if __name__ == "__main__":
    get_coordinates()
