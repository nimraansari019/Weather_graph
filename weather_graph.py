import requests
import matplotlib.pyplot as plt

#  Your API key
API_KEY = "a4dedab625d3478e7f8ac1f2ac048b37"

#  List of cities
cities = ["Mumbai", "Delhi", "Chennai", "Kolkata", "Bangalore"]

# Store temperatures
temps = []

#  Get weather data for each city
for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data["main"]["temp"]
        temps.append(temp)
        print(f"{city}: {temp}°C")
    else:
        print(f"Failed to get weather for {city}. Reason: {data.get('message')}")
        temps.append(0)  # To avoid crash during plotting

#  Plot the data
plt.figure(figsize=(10, 5))
plt.bar(cities, temps, color="skyblue")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.title("Current Temperature in Indian Cities")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
