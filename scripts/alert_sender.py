import requests
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / "tokens.env"
load_dotenv(dotenv_path=env_path)

class AlertSender:
    def __init__(self):
        self.bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.user_id = os.getenv("USER_INFO_ID")

    def send_telegram_alert(self, message):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        payload = {
            "chat_id": self.user_id,
            "text": message
        }
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            raise Exception(f"Failed to send alert: {response.text}")
        else:
            print("Alert sent successfully.")
        return response.json()