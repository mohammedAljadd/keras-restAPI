import requests

BASE = "http://192.168.43.203:5000/face"

image = {'image': open('me.jpg', 'rb')}

response = requests.post(BASE, files=image)

print(response.json())