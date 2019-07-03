from bs4 import BeautifulSoup
import requests
from csv import writer

response = requests.get("https://www.responsify.com/blog/")

soup = BeautifulSoup(response.text, 'html.parser')  

with open('posts.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Link', 'Date']
    csv_writer.writerow(headers)

posts = soup.find_all(class_="type-blogteaser-standard-headline text-center responsify-serif")

for post in posts:
    link = post.find_all("a")["href"]
    print(link)
    print(post.text)
    csv_writer.writerow([link])

