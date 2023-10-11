import requests
from bs4 import BeautifulSoup


url = 'https://mausam.imd.gov.in/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    article_titles = soup.find_all('h2')
    
    for title in article_titles:
        print(title.text)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
