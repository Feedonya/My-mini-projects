import requests
import json

def main():
    city = input("Введите город на русском: ")
    print("")

    url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

    #print(url) - проверяем ссылку, если нужно

    weather_data = requests.get(url).json()

    weather_data_structure = json.dumps(weather_data)

    weather = weather_data["main"]["temp"]
    weather_like = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]
    main = weather_data["weather"]

    print("Текущая погода: ", main[0]["main"])
    print("Текущая температура: ", round(weather))
    print("Ощущается как: ", round(weather_like))
    print("Влажность: ", humidity)
    print("Приятного дня!")

if __name__ == "__main__":
    main()

"""
Данные выглядят так:
{"coord": {"lon": 46.0333, "lat": 51.5667}, "weather": [{"id": 804, "main": "Clouds", "description": "\u043f\u0430\u0441\u043c\u0443\u0440\u043d\u043e", "icon": "04n"}], "base": "stations", "main": {"temp": 20.53, "feels_like": 19.84, "temp_min": 16.52, "temp_max": 20.53, "pressure": 1012, "humidity": 46}, "visibility": 10000, "wind": {"speed": 1.45, "deg": 54, "gust": 1.43}, "clouds": {"all": 100}, "dt": 1690938901, "sys": {"type": 2, "id": 2001834, "country": "RU", "sunrise": 1690939201, "sunset": 1690994652}, "timezone": 14400, "id": 498677, "name": "\u0421\u0430\u0440\u0430\u0442\u043e\u0432", "cod": 200}
""" 
