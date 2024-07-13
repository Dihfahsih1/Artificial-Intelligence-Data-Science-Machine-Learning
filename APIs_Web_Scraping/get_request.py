import requests

url = "https://dihfahsih.com/api/reviews-list-secured/"

token="a847aa77929479dcf4ac15a3f5c71b28ea646771"
token_payload={
    'Authorization': f'Token {token}'    
}
response = requests.get(url, headers=token_payload)

if response.status_code == 200:
    data = response.json() 
    print(data[-1])    
else:
    print("Failed to create a get")
    print("Status Code: ", response.status_code)
    print("Response: ", response.text)