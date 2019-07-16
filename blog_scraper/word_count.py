from bs4 import BeautifulSoup
import requests

'''
get_links return a lst of all the relevant links 
only works if it has /blog or /blogs next to its domain name
else returns None
in the end it will return a word count of all the words in 
'''
# works if blog or blogs is after the website name
def get_links(keyword, response):
    blacklist = {'author', 'topic', 'all'} # set of words to avoid 
    # response = requests.get("http://360alumni.com/blog")    
    soup = BeautifulSoup(response.text, 'html.parser')
    blog_links = set() # set so no duplicates
    next_page_lst = set()
    for a in soup.find_all('a', href=True):
        try:
            if keyword in a['href'].split('/')[3].lower(): # has /blog or /blogs
                try: # has something after the /blog
                    if 'page' in a['href'].split('/')[4].lower(): # get next_page
                        next_page_lst.add(a['href'])
                    else:
                        add = True
                        for i in blacklist: # test all words in blacklist
                            if i in a['href'].split('/')[4].lower(): # don't add if contains blacklist word
                                add = False
                                break 
                        if add: blog_links.add(a['href'])  # get link to a blog
                except Exception as e: print(4, e, a['href'])
        except Exception as e: print(3, e, a['href'])

    for i in blog_links: print(i)
    return blog_links

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
    return word_count

# Finding words based on the blog post count
# returns a list of words for each blog
def find_words(link_lst):
    lst = []
    for link in link_lst:
        try:
            response = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            num_words =  get_num_of_words(soup) 
            lst.append((num_words, link))
        except Exception as e:
            lst.append(('N/A', link))
            print(e)
    return lst

# x = get_links('blog', requests.get("http://360alumni.com/blog"))
# print(x)
# y = find_words(x)
# print(y)
