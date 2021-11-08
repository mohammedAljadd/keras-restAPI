import requests

BASE = "http://192.168.43.203:5000/"


response = requests.post(BASE)

print(response.json()["data"])
