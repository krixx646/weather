
import tkinter as tk
from tkinter import messagebox
from logic import fetch_weather
from utils import load_preferences, save_preferences

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.city_label = tk.Label(root, text="Enter City:")
        self.city_label.pack()

        self.city_entry = tk.Entry(root)
        self.city_entry.pack()

        self.search_button = tk.Button(root, text="Search", command=self.get_weather)
        self.search_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        # Load last searched city
        last_city = load_preferences()
        if last_city:
            self.city_entry.insert(0, last_city)
            self.get_weather()

    def get_weather(self):
        city = self.city_entry.get()
        weather = fetch_weather(city)
        if weather:
            self.result_label.config(text=f"Temperature: {weather['temp']}°C\nDescription: {weather['description']}")
            save_preferences(city)
        else:
            messagebox.showerror("Error", "Could not fetch weather data")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
