from bs4 import BeautifulSoup
import requests

# url="http://example.com/"
# response=requests.get(url)
# soup=BeautifulSoup(response.text, 'html.parser')

with open("index.html") as fp:
    soup=BeautifulSoup(fp, 'html.parser')
    heading=soup.find('h2') # this finds the first <h1> tag
    soup.find_all('p') #finds all <p> tags
    tag=soup.find('a')
    
    #Accessing the Attributes of a tag
    url=tag['href'] # print the value of the href attribute
    
    #Extracting text
    print(heading.text)
    