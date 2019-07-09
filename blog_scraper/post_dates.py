from bs4 import BeautifulSoup
import requests

response = requests.get("http://blogs.reuters.com/")
soup = BeautifulSoup(response.text, 'html.parser')

def find_dates(url):
    title =[n.text for n in soup.find_all("h2")]
    date = [x.text for x in soup.find_all("div",attrs={"class":"timestamp"})]
    print(date)
    print(title)

find_dates(response)



