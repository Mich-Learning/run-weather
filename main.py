"""Run weather report — fetch weather from Open-Meteo."""
import requests


def fetch_weather(latitude, longitude):
    """Fetch current weather from Open-Meteo."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
        "timezone": "auto",     
    }

    response = requests.get(url, params=params)
    print("Status code:", response.status_code)
    print()

    data = response.json()
    return data


def run_verdict(temperature, wind_speed):
    """Decide if it's a good day to run based on weather."""
    if temperature < -5:
        return "🥶 Too cold — run indoors."
    if temperature > 30:
        return "🥵 Too hot — run early morning or indoors."
    if wind_speed > 40:
        return "💨 Very windy — expect a tough run."
    if 5 <= temperature <= 20 and wind_speed < 25:
        return "✅ Great day to run!"
    return "👍 Fine — reasonable conditions."


def main():
    data = fetch_weather(latitude=43.65, longitude=-79.38)

    current = data["current"]
    units = data["current_units"]

    temp = current["temperature_2m"]
    wind = current["wind_speed_10m"]

    print("=== Current Weather ===")
    print(f"Time:        {current['time']}")
    print(f"Temperature: {temp} {units['temperature_2m']}")
    print(f"Wind speed:  {wind} {units['wind_speed_10m']}")
    print()
    print("=== Verdict ===")
    print(run_verdict(temp, wind))


if __name__ == "__main__":
    main()