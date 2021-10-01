import requests
import json

TOKEN = "3054a0d63a2e4de482979c023c8f8504"
SMS_API_URL = f'https://console.melipayamak.com/api/send/shared/{TOKEN}'

header = {'Content-type': 'application/json; utf-8',
          'Accept': 'application/json'}


def sms_one_time_password(to: str, password: str) -> bool:
    body = {
        "bodyId": 58751,
        "to": to,
        "args": [password]
    }
    response = requests.post(SMS_API_URL,
                             json.dumps(body),
                             headers=header)
    return response.ok
