# Chill with Python – Branded Weather App Tutorial Version

# Import tkinter for GUI creation and Canvas for gradient background
import tkinter as tk
from tkinter import Canvas

# Import requests library to fetch data from OpenWeatherMap API
import requests

# -----------------------------
# Function: Fetch weather data and update GUI
# -----------------------------
def get_weather():
    # Get the city name entered by the user in the input box
    city = city_entry.get()
    
    # Set up OpenWeatherMap API URL with your API key
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Construct the complete API request URL
    complete_url = f"{base_url}appid={api_key}&q={city}"

    # Send HTTP GET request to the API
    response = requests.get(complete_url)
    
    # Convert the API response to JSON format for easier parsing
    data = response.json()

    # Check if the city is found (code not equal to 404)
    if data["cod"] != "404":
        # Extract main weather data from the JSON response
        main = data["main"]
        temp_c = main["temp"] - 273.15  # Convert temperature from Kelvin to Celsius
        humidity = main["humidity"]      # Get humidity percentage
        weather_desc = data["weather"][0]["description"]  # Get weather description
        
        # Choose a simple emoji icon based on the weather description
        icon = "☀️" if "clear" in weather_desc.lower() else \
               "☁️" if "cloud" in weather_desc.lower() else \
               "🌧️"

        # Update the result_label with the formatted weather information
        result_label.config(
            text=f"{icon} Weather in {city.title()}:\n"
                 f"Temperature: {temp_c:.2f}°C\n"
                 f"Humidity: {humidity}%\n"
                 f"Description: {weather_desc.title()}"
        )
    else:
        # If city is not found, display an error message
        result_label.config(text="City not found. Please try again.")

# -----------------------------
# GUI Setup
# -----------------------------
# Create the main application window
root = tk.Tk()
root.title("Chill with Python - Weather App")  # Set the window title
root.geometry("450x300")                        # Set window size
root.resizable(False, False)                    # Prevent resizing

# -----------------------------
# Gradient Background using Canvas
# -----------------------------
# Create a Canvas widget to simulate gradient background
canvas = Canvas(root, width=450, height=300)
canvas.pack(fill="both", expand=True)

# Loop through pixels vertically to create a smooth teal → purple gradient
for i in range(300):
    r = int(79 + (167-79)*i/300)    # Red value interpolation
    g = int(209 + (142-209)*i/300)  # Green value interpolation
    b = int(197 + (250-197)*i/300)  # Blue value interpolation
    color = f'#{r:02x}{g:02x}{b:02x}'
    canvas.create_rectangle(0, i, 450, i+1, outline=color, fill=color)

# -----------------------------
# Heading Label
# -----------------------------
# Display the title of the app inside the window
heading = tk.Label(
    root, 
    text="Python Weather App", 
    font=("Helvetica", 16, "bold"), 
    bg="#4fd1c5",  # Matching branded color
    fg="white"
)
heading.place(relx=0.5, rely=0.1, anchor="center")  # Center it horizontally

# -----------------------------
# City Input Box
# -----------------------------
# Entry widget for the user to type the city name
city_entry = tk.Entry(root, width=25, font=("Helvetica", 12))
city_entry.place(relx=0.5, rely=0.25, anchor="center")  # Center input box
city_entry.insert(0, "Enter city name")  # Placeholder text

# -----------------------------
# Button to Get Weather
# -----------------------------
# Button widget that triggers get_weather function when clicked
get_button = tk.Button(
    root, 
    text="Get Weather", 
    command=get_weather, 
    font=("Helvetica", 12), 
    bg="#4FD1C5",  # Brand color
    fg="white"
)
get_button.place(relx=0.5, rely=0.35, anchor="center")  # Center button

# -----------------------------
# Label to Display Results
# -----------------------------
# Label widget to display weather output (temperature, humidity, description)
result_label = tk.Label(
    root, 
    text="", 
    font=("Helvetica", 12), 
    justify="left", 
    bg="#e0e0e0"  # Light background for readability
)
result_label.place(relx=0.5, rely=0.6, anchor="center")  # Center result label

# -----------------------------
# Start the GUI loop
# -----------------------------
# This keeps the window open and responsive
root.mainloop()
