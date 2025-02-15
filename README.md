Weather App

A simple command-line weather application that fetches real-time weather data using the OpenWeatherMap API. 🌦️

Features

Get current weather details by entering a city name.

Displays temperature, weather condition, humidity, and wind speed.

Error handling for invalid API keys, network issues, and incorrect city names.

Technologies Used

Python 🐍

Requests Library 🌍

OpenWeatherMap API ☁️

Installation

Clone the repository:

git clone https://github.com/your-username/weather-app.git
cd weather-app

Install required dependencies:

pip install requests

Get an OpenWeatherMap API Key:

Sign up at OpenWeatherMap.

Go to API Keys and generate a key.

Update API Key in weather_app.py:

API_KEY = "your_actual_api_key_here"

Usage

Run the script:

python weather_app.py

Enter a city name when prompted.

Enter city name (or 'quit' to exit): London

Example Output:

Weather in London:
Temperature: 15°C
Condition: Clear sky
Humidity: 60%
Wind Speed: 3.5 m/s

Error Handling

⚠️ Invalid API Key? Double-check your key.

⚠️ City Not Found? Try a different city name.

⚠️ Network Error? Check your internet connection.

Contributing

Feel free to fork this repository and submit pull requests! 💡

License

This project is licensed under the MIT License. 📜

