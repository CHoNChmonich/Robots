import requests
import json

url = 'http://127.0.0.1:8000/robots/api/create_robot/'
data = {"model":"14","version":"8b","created":"2024-12-11 00:00:00"}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

# Проверка ответа
if response.status_code == 201:
    print("Robot created:", response.json())
else:
    print("Error:", response.status_code)
    print(response.text)
