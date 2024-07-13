import requests
from bs4 import BeautifulSoup

url="https://dihfahsih.com/"
response=requests.get(url)

if response.status_code == 200:
    #Parsing the html content
    soup=BeautifulSoup(response.text, "html.parser")
    
    #extract and print the title of the page
    Name=soup.find('h1',class_='text-white font-weight-bold').text
    header_two=soup.find('h2',class_="text-light").text
    paragraph=soup.find('p', class_="text-muted").text
    print(f"Name form the page: {Name}, Header : {header_two}, Paragraph: {paragraph}")
    
    #extracting and printing all the links on the page'
    # links=soup.find_all('a')
    # for link in links:
    #     href=link.get('href')
    #     text=link.text
    #     print(f"Link text: {text}, URL: {href}")
        
else:
    print(f"Failed to retrieve the webpage. Status Code: {response.status_code}")
    