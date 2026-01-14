import requests
from tkinter import *
from tkinter import messagebox

# -----------------------------
# Function to get weather info
# -----------------------------
def get_weather():
    city = city_entry.get()
    if city == "":
        messagebox.showerror("Error", "Please enter a city name!")
        return

    api_key = "66596a675d73d271edf46a153ed828ad"  # 🔹 Replace with your active API key
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={api_key}&units=metric"

    try:
        response = requests.get(base_url)
        data = response.json()

        if data["cod"] == 200:
            city_name = data["name"]
            country = data["sys"]["country"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"].capitalize()

            result_label.config(
                text=f"🌆 City: {city_name}, {country}\n"
                     f"🌡 Temp: {temperature}°C\n"
                     f"💧 Humidity: {humidity}%\n"
                     f"🌥 Condition: {description}"
            )
        else:
            messagebox.showerror("Error", f"City '{city}' not found!")

    except Exception as e:
        messagebox.showerror("Error", "Network issue or invalid API key!")

# -----------------------------
# GUI Design
# -----------------------------
root = Tk()
root.title("Weather Forecast App")
root.geometry("400x400")
root.config(bg="#87CEEB")

# Title
Label(root, text="🌦 Weather Forecast App", font=("Helvetica", 16, "bold"), bg="#87CEEB").pack(pady=15)

# Entry Box
city_entry = Entry(root, font=("Helvetica", 14), justify="center")
city_entry.pack(pady=10)
city_entry.focus()

# Button
Button(root, text="Get Weather", font=("Helvetica", 12, "bold"),
       command=get_weather, bg="#4682B4", fg="white", relief="raised").pack(pady=10)

# Result Label
result_label = Label(root, text="", font=("Helvetica", 12), bg="#87CEEB", justify="center")
result_label.pack(pady=20)

# Footer
Label(root, text="Developed by Shubham Tiwari", font=("Helvetica", 9), bg="#87CEEB").pack(side="bottom", pady=10)

root.mainloop()