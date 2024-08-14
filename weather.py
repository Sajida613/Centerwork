 
# Weather Program

# Import libraries
import requests
import json

# API endpoint
api_endpoint = "(link unavailable)"

# API key
api_key = "YOUR_API_KEY_HERE"

# Function to get weather data
def get_weather(city):
  params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
  }
  response = requests.get(api_endpoint, params=params)
  data = json.loads(response.text)
  return data

# Function to display weather data
def display_weather(data):
  print("City:", data["name"])
  print("Temperature:", data["main"]["temp"], "°C")
  print("Humidity:", data["main"]["humidity"], "%")
  print("Weather:", data["weather"][0]["description"])

# Main program
while True:
  print("1. Get Weather")
  print("2. Exit")
  choice = input("Enter your choice: ")
  if choice == "1":
    city = input("Enter city name: ")
    data = get_weather(city)
    display_weather(data)
  elif choice == "2":
    break
  else:
    print("Invalid choice. Please try again.")





