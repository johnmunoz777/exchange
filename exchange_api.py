#https://api.exchangerate-api.com/v4/latest/usd
#https://api.exchangerate-api.com/v4/latest/cad
import requests
endpoint_url = 'https://api.exchangerate-api.com/v4/latest/cad'
response = requests.get(endpoint_url)
print(response)
print(type(response))
response
response_json = response.json()
print(response_json)
print(type(response_json))
response_json.keys()

endpoint_url = 'https://api.exchangerate-api.com/v4/latest/gbp'
response = requests.get(endpoint_url)
response_dict = response.json()

print(type(response))
print(type(response_dict))

for key in response_dict:
    print(key, ":", response_dict[key])

endpoint_url='https://api.exchangerate-api.com/v4/latest/usd'
response = requests.get(endpoint_url)
response_json = response.json()
response_json['rates']

for key, value in response_json['rates'].items():
    if value >=3 and value < 4:
         print(key, value)
         
response_json['rates']['PEN']
for key, value in response_json['rates'].items():
    print(key.lower(), value)