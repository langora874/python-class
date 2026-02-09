import requests

# Example API URL

url = "https://jsonplaceholder.typicode.com/posts"
# GET – read data
response = requests.get(url)
print("GET:", response.status_code)

# POST – send new data
new_post = {"title": "Hello", "body": "Learning HTTP", "userId": 1}
response = requests.post(url, json=new_post)
print("POST:", response.status_code)

# PUT – update data
updated_post = {"title": "Updated Title", "body": "New content", "userId": 1}
response = requests.put(f"{url}/1", json=updated_post)
print("PUT:", response.status_code)

# DELETE – delete data
response = requests.delete(f"{url}/1")
print("DELETE:", response.status_code)
