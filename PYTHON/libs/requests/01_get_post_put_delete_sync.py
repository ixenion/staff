import requests

response = requests.get('https://api.example.com/items')
print(response.json())  # Вывод полученных данных в формате JSON


data = {"key": "value"}
response = requests.post('https://api.example.com/items', json=data)
print(response.json())  # Вывод полученных данных в формате JSON


data = {"key": "updated_value"}
response = requests.put('https://api.example.com/items/1', json=data)
print(response.json())  # Вывод полученных данных в формате JSON


response = requests.delete('https://api.example.com/items/1')
print(response.status_code)  # Вывод статус кода ответа (например, 200 - успех)

