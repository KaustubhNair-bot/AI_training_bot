from api_client import OpenWeatherClient

if __name__ == "__main__":
    client = OpenWeatherClient()

    cities = ["London", "New York", "Tokyo", "Paris", "Sydney"]

    for city in cities:
        data = client.fetch_weather_by_city(city)
        client.save_raw_response(city, data)
        print(f"Fetched and saved weather data for {city}")
