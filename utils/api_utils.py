import requests, os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")

def api_calling(prompt):
        payload = {
            "question": prompt,
            "overrideConfig": {
                "sessionId": "567"
            }
        }
        response = requests.post(API_URL, json=payload)
        return response.json()['text']