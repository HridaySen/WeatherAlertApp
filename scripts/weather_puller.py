from geopy.geocoders import Nominatim
import requests

class WeatherPuller:
    def __init__(self, location):
        self.location = location
        self.geolocator = Nominatim(user_agent="weather_app")

    def pull_weather_data(self):
        latitude, longitude = self.convert_location_to_coordinates()
        self.url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weather_code,daylight_duration,sunshine_duration,snowfall_sum,precipitation_sum,precipitation_hours&hourly=temperature_2m&current=temperature_2m,rain,showers,precipitation&timezone=auto"
        return requests.get(self.url).json()
        
    def convert_location_to_coordinates(self):
        self.geo_location = self.geolocator.geocode(self.location)
        return self.geo_location.latitude, self.geo_location.longitude