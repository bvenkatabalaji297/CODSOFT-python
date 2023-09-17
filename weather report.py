import requests

# Function to fetch weather data from the OpenWeatherMap API
def fetch_weather_data(location, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Create parameters for the API request based on the location and API key
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # Use 'metric' for Celsius and 'imperial' for Fahrenheit
    }

    # Make the API request
    response = requests.get(base_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data.")
        return None

# Function to display weather information
def display_weather_info(data):
    if data is not None:
        # Extract relevant weather information from the API response
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']

        # Display weather information to the user
        print(f"Weather in {data['name']}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("No weather data to display.")

# Main program
if __name__ == "__main__":
    api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key

    # Prompt the user to enter a city name or zip code
    location = input("Enter a city name or zip code: ")

    # Fetch weather data and display it
    weather_data = fetch_weather_data(location, api_key)
    display_weather_info(weather_data)
