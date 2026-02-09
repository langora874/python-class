import requests

url = "https://jsonplaceholder.typicode.com/users"

# GET data
response = requests.get(url)
print(response.json()[0])  # print first user
