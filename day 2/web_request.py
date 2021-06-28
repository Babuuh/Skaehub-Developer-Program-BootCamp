import requests

response = requests.get('https://www.google.com/')

print("Text Response")
print(response.text)

print("\n==============================================================================")
print("\nWeb Content")
print(response.content)

print("\n==============================================================================")
print("\nRaw Data")

res = requests.get('https://fast.com/', stream=True)
print(res.raw)
print(res.raw.read(15))
