from bs4 import BeautifulSoup
import requests
# from csv import writer

def get_posts():
    response = requests.get("https://www.responsify.com/blog/")

    soup = BeautifulSoup(response.text, 'html.parser')

    # with open('posts.csv', 'w') as csv_file:
    #     csv_writer = writer(csv_file)
    #     head
    # ers = ['Title', 'Link', 'Date']
    #      csv_writer.writerow(headers)
    posts = soup.find_all(class_="type-blogteaser-standard-headline text-center responsify-serif")

    #link = soup.find_all('a')

    links = [a.get('href') for a in soup.find_all('a', href=True)]
    print(links)

    # linklist = []
    # for link in soup.find_all('a'):
    #     print(link.get('href'))8

    return posts #returns a list of posts

    # for post in posts:
    #     print(post.text)
    #     # csv_writer.writerow([link])

