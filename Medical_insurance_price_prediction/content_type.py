import requests

headers = {
    "Content-Type": "application/json"
}

url = "https://example.com/api/endpoint"
# Define the JSON data to send in the request body
json_data = {
    "name": "John Doe",
    "age": 30
}

response = requests.post(url, headers=headers, data=json_data)