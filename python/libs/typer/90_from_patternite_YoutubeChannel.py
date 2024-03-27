# weather.py
import typer
from enum import Enum
import requests

"""
Creating a Mars Weaather CLI
"""
app = typer.Typer(add_completion=False)
preassure_app = typer.Typer()
temperature_app = typer.Typer()
app.add_typer(preassure_app, name="preassure")
app.add_typer(temperature_app, name="temperature")

# we reffer to Martians days as "sols"
URL = "https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"
responce = requests.get(URL).json()
# print(responce)
sols = list(filter(lambda x: x.isnumeric(), responce.keys()))   # filter non-weather data
# print('sols',sols)
# current_sol_data = responce[sols[-1]]   # most resent sol is tha last element of 'sols'
current_sol_data = {
            "Northern_season": 'late winter',
            "Southern_season": 'hz'
        }

# we define an Enum which specifies the walid options for the MArs hemisphere
class Hemisphere(Enum):
    north = "north"
    south = "south"

# use decoartor to indicate that
# the function is the part of the typer app
# By passing in our 'Hemisphere' Enum, typer will ensure either "north" or "south"
# is passed as a CLI option, or the command will fail. Running --help will also show
# "north" and "south" as the valid option.
@app.command()
def season(hemisphere: Hemisphere):
    if hemisphere.value =="north":
        typer.echo(current_sol_data["Northern_season"])
    else:
        typer.echo(current_sol_data["Southern_season"])


if __name__ == "__main__":
    app()
