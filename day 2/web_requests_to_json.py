import requests, json

response = requests.get('https://api.github.com/events')

#splitting the data
data = json.dumps(response.text)
dict_object =  data.split()


print(dict_object[0])