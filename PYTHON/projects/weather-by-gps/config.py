USE_ROUNDED_COORDS = True
LOCATION = "Moscow"

# best practice is store apis at environment variables
# OPENWEATHER_API = os.getenv("OPENWEATHER_API")
# but for simplicity
OPENWEATHER_API = "7549b3ff11a7b2f3cd25b56d21c83c6a"
OPENWEATHER_URL_TEMPLATE = (
        "https://api.openweathermap.org/data/2.5/weather?"
        "lat={latitude}&lon={longitude}&"
        "appid=" + OPENWEATHER_API + "&lang=ru&"
        "units=metric"
        )

