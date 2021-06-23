import requests

try:
    response = requests.get('https://www.kaggle.com/', timeout=10)
    print(response.text)

except requests.exceptions.Timeout as e:
    print(e)