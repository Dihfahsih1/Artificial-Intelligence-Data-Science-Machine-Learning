import requests

url = "https://dihfahsih.com/api/review-secure-post/"

data = {
    "first_name": "Merry",
    "last_name": "James",
    "relationship": "Test2",
    "compliment": "cool api call"
}

token="a847aa77929479dcf4ac15a3f5c71b28ea646771"
# Headers including the authentication token
headers = {
    'Authorization': f'Token {token}',
    'Content-Type': 'application/json'
}
response = requests.post(url, json=data, headers=headers)
if response.status_code == 201:
    new_post = response.json()
    print("New Post created: ", new_post)
else:
    print("Failed to create a post")
    print("Status code:", response.status_code)
    print("Response:", response.text)
