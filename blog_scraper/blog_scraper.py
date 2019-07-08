from bs4 import BeautifulSoup
import requests
import re

response = requests.get("http://blogs.reuters.com/")
soup = BeautifulSoup(response.text, 'html.parser')
links = [a.get('href') for a in soup.find_all('a', href=True)]  

# posts = soup.find_all(class_="type-blogteaser-standard-headline text-center responsify-serif")


def find_words():
    
    bloglist = links[0]
    blogrequest = requests.get(bloglist)
    
    soup_two = BeautifulSoup(blogrequest.text, 'html.parser') 
    
    if blogrequest.status_code == 200:
        print('Success!')
    elif blog_request.status_code == 404:
        print('Not Found.')
    
    find_words = soup_two.find_all('p')
    
    store = ""

    for n in find_words:
        store += n.get_text()


    word_count = str(len(store.split()))
    print ("word count = " + word_count)

find_words()
