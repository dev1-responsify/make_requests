from bs4 import BeautifulSoup
import requests

#getting requests from a certain website and integrating beautiful soup
response = requests.get("http://blogs.reuters.com/")
soup = BeautifulSoup(response.text, 'html.parser')
#for loop to find all the a href links
links = [a.get('href') for a in soup.find_all('a', href=True)]  


#Finding words based on the blog post count
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



