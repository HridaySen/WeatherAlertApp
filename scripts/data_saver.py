import json
import os

class DataSaver:
    def __init__(self, data, file_path=os.path.join("D:\\Coding\\Portfolio Projects\\Weather Alert App\\Saved Json Files", "weather_data.json")):
        self.data = data
        self.file_path = file_path

    def save_to_json(self):
        with open(self.file_path, "w") as json_file:
            json.dump(self.data, json_file, indent=4)
        print(f"Weather data saved to {self.file_path}")