import requests
url = "https://dihfahsih.com/api/review-secure-post/"
data={
    "first_name": "Smith",
    "last_name" : "Johnson",
    "relationship": "Teamate",
    "compliment": "Testing the secured api call"
}

token="a847aa77929479dcf4ac15a3f5c71b28ea646771"
token_payload={
    'Authorization': f'Token {token}'    
}

response=requests.post(url,json=data,headers=token_payload)
if response.status_code==201:
    new_post=response.json()
    print("Data Submited: ", new_post)    
else:
    print("Failed to create a post")
    print("Status Code: ", response.status_code)
    print("Response: ", response.text)
    