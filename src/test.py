import requests

url = 'http://localhost:9696/predict'

data = {'url': 'http://clipart-library.com/images/gieERjykT.jpg'}

result = requests.post(url, json=data).json()
print(result)