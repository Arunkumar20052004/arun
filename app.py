import tkinter as tk
import requests
API_KEY = "your_api_key_here"

def get_weather():
    city = city_entry.get()
    if city:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            result_label.config(text=f"Weather: {weather}\nTemperature: {temp}°C")
        else:
            result_label.config(text="City not found!")
    else:
        result_label.config(text="Enter a city name.")

root = tk.Tk()
root.title("Weather App")

tk.Label(root, text="Enter City Name:").pack()

city_entry = tk.Entry(root)
city_entry.pack()

tk.Button(root, text="Get Weather", command=get_weather).pack()

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack()

root.mainloop()
