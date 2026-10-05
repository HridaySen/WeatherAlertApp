import json
import os
from scripts.weather_puller import WeatherPuller
from scripts.data_saver import DataSaver
from scripts.alert_sender import AlertSender

while True:
    location = input("Enter a location (or type 'exit' to quit): ")
    if location.lower() == 'exit':
        break

    weather_puller = WeatherPuller(location)
    weather_data = weather_puller.pull_weather_data()

    data_saver = DataSaver(weather_data)
    data_saver.save_to_json()

    #detect if rain is expected in the next week and send a telegram alert
    with open(os.path.join("D:\\Coding\\Portfolio Projects\\Weather Alert App\\Saved Json Files", "weather_data.json"), "r") as json_file:
        data = json.load(json_file)
        daily_data = data.get("daily", {})
        rain_data = daily_data.get("precipitation_sum", [])
        if any(rain > 0 for rain in rain_data):
            print("Rain is expected in the next week. Sending telegram alert...")
            # code to send telegram alert goes here
            alert_sender = AlertSender()
            alert_sender.send_telegram_alert(f"Rain is expected in {location} in the next week. Please take necessary precautions.")