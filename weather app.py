import requests

def get_weather(city):
    API_KEY = "75169eab627057def924b16873b2e856"  # Replace with your actual API key
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"  # Correct API URL

    params = {
        "q": city,         
        "appid": API_KEY,  
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()  # Convert response to JSON

        if response.status_code == 200:
            city_name = data["name"]
            temp = data["main"]["temp"]
            weather_desc = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            print(f"\nWeather in {city_name}:")
            print(f"Temperature: {temp}°C")
            print(f"Condition: {weather_desc.capitalize()}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s\n")
        
        elif response.status_code == 401:
            print("\n⚠️ Invalid API Key! Please check and update your API key.")

        elif response.status_code == 404:
            print("\n⚠️ City not found! Please enter a valid city name.")

        else:
            print(f"\n⚠️ Error {response.status_code}: {data.get('message', 'Unknown error')}")

    except requests.exceptions.RequestException as e:
        print("\n⚠️ Network error! Please check your internet connection.")
        print(f"Error details: {e}")

# Main loop
while True:
    city = input("Enter city name (or 'quit' to exit): ").strip()
    if city.lower() == "quit":
        print("Goodbye! Stay safe! ☀️")
        break
    get_weather(city)
