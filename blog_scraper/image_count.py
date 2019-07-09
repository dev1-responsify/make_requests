from bs4 import BeautifulSoup
import requests


response = requests.get("http://blogs.reuters.com/")
soup = BeautifulSoup(response.text, 'html.parser')
links = [a.get('href') for a in soup.find_all('a', href=True)]  

# posts = soup.find_all(class_="type-blogteaser-standard-headline text-center responsify-serif")

def image_count(url):




