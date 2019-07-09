from bs4 import BeautifulSoup
import requests



response = requests.get("http://blogs.reuters.com/")
soup = BeautifulSoup(response.text, 'html.parser')


def image_count(url):
    img_tags = soup.find_all('img')
    urls = [img['src'] for img in img_tags]
    num_images = str(len(urls))
    print('image count = ' +  num_images)

image_count(response)



