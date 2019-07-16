from bs4 import BeautifulSoup
import requests

<<<<<<< HEAD
#getting requests from a certain website and integrating beautiful soup
response = requests.get("http://blogs.reuters.com/")
soup = BeautifulSoup(response.text, 'html.parser')
#for loop to find all the a href links
links = [a.get('href') for a in soup.find_all('a', href=True)]  

=======

# response = requests.get("http://blogs.reuters.com/")
response = requests.get("https://www.afterellen.com/")
soup = BeautifulSoup(response.text, 'html.parser')
links = [a.get('href') for a in soup.find_all('a', href=True)] 
for i in links: print(i)
# posts = soup.find_all(class_="type-blogteaser-standard-headline text-center responsify-serif")
>>>>>>> 2fa646d3632e7e9a3031c6b634de5ba8dd910cfb

# checks if url has blogs in the url
def check_url(url):
    url += 'blogs'
    response = requests.get(url)
    if response.status_code != 200:
        return 'error'
    return url

# returns the number of words in the blog 
# includes some extra stuff like title of next and previous post
def get_num_of_words(soup_two):
    # black_lst = ['comment', 'caption', 'disclaimer']
    find_words = soup_two.find_all('p')
    # print(find_words)
    store = ''
    for i in find_words:
        try:
            class_name_lst = i.find_previous('div')['class'] # returns a list with all the class names
            flag = True
            for name in class_name_lst:
                if ('comment' in name.lower()) and ('caption' in name.lower()) and ('disclaimer' in name.lower()): 
                    flag = False  
                    break
            if flag: store += i.text           
        except: pass
    print(store)
    word_count = str(len(store.split()))
    print ("word count = " + word_count)

<<<<<<< HEAD
    
=======

# Finding words based on the blog post count
def find_words():
>>>>>>> 2fa646d3632e7e9a3031c6b634de5ba8dd910cfb
    bloglist = links[0]
    blogrequest = requests.get(bloglist)
    
    soup_two = BeautifulSoup(blogrequest.text, 'html.parser') 
    
    if blogrequest.status_code == 200:
        print('Success!')
    elif blog_request.status_code == 404:
        print('Not Found.')
    
    get_num_of_words(soup_two)
    
            
        
    
    

# find_words()



