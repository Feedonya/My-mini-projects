from tkinter import *
from tkinter import messagebox
import requests
import json

def show_message():
    city = message.get()
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    weather_data = requests.get(url).json()

    weather_data_structure = json.dumps(weather_data)

    weather = weather_data["main"]["temp"]
    weather_like = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]
    main = weather_data["weather"]
    data = [f"Текущая погода: {main[0]['main']}","\n",
    f"Текущая температура: {round(weather)}","\n",
    f"Ощущается как: {round(weather_like)}","\n",
    f"Влажность: {humidity}","\n",
    "Приятного дня!"]
    messagebox.showinfo("Погода", data)

root = Tk()
root.title("Погода")
root.geometry("300x250")

message = StringVar()

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="c")

message_button = Button(text="Узнать погоду", command=show_message)
message_button.place(relx=.5, rely=.5, anchor="c")

root.mainloop()