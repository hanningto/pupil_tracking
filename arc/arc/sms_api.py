import requests
import json
 
username = "NG5ibjNSTUsybGJ6UW5Hd0QyOXU6SmJRS0owSjAyWU5Iek42R2g4Z0NZVVRyN3ZQWlA2V0dCUXQ1MnNVag=="
password = "JbQKJ0J02YNHzN6Gh8gCYUTr7vPZP6WGBQt52sUj"
body = {
    "message": "Test message",
    "source": "SMS_TEST",
    "destination": [
        {
            "number": "254700882765",
        },
    ]
}
 
url = "https://api.smsleopard.com/v1/sms/send"
r = requests.post(url, data=json.dumps(body), auth=requests.auth.HTTPBasicAuth(username, password))
data = r.json()
print(data)