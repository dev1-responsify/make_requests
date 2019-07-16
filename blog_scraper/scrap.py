from bs4 import BeautifulSoup
import requests
<<<<<<< HEAD
import pandas as pd
=======
import lxml.html
import requests
import pandas as pd
from io import StringIO
>>>>>>> ef801acd69708f53f23d9cb099d8321301dd087e
from word_count import find_words, get_links

# make a csv file
def make_csv(csv_file, lst):
    df = pd.read_csv(csv_file)
<<<<<<< HEAD
    for i in lst: print(lst)
=======
>>>>>>> ef801acd69708f53f23d9cb099d8321301dd087e
    df['result'] = lst
    df.to_csv('output.csv')

def df_creation(fileString):
    # temp = StringIO(fileString)
    df = pd.read_csv(fileString)
    return df['Company domain name'].to_list()

# checks if url has blogs in the url
def check_url(url):
    print('in url: ', url)
    url1 = url + "/blog"
    url2 = url + '/tag/blog'
    url3 = url + '/blogs'
    try:
        # if page exists with the filter then send that response to count_words
        requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        response = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        if response.status_code == 200: 
            links = get_links('blog', response)
            num_words_lst = find_words(links)
<<<<<<< HEAD
            print('-------------------', num_words_lst, links)
            return num_words_lst, url1
=======
            return num_words_lst
>>>>>>> ef801acd69708f53f23d9cb099d8321301dd087e
            # return url1
        response2 = requests.get(url2,  headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        if response2.status_code == 200: 
            links = get_links('blog', response)
<<<<<<< HEAD
            return find_words(links), url2
        response3 = requests.get(url3, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        if response3.status_code == 200: 
            links = get_links('blogs', response)
            return find_words(links), url3
=======
            return find_words(links)
        response3 = requests.get(url3, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        if response3.status_code == 200: 
            links = get_links('blogs', response)
            return find_words(links)
>>>>>>> ef801acd69708f53f23d9cb099d8321301dd087e
        
        # if link is already the blog- check title to see if blog in name
        response4 = BeautifulSoup(requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10).text, 'html.parser')
        for i in response4.find_all("title"):
            if 'blog' in i.text.lower(): 
                links = get_links(response)
<<<<<<< HEAD
                return find_words(links), url
=======
                return find_words(links)
>>>>>>> ef801acd69708f53f23d9cb099d8321301dd087e
        
        
    except Exception as e:
        print(e)
        return 'N/A' # timeout or error so return N/A since site not accessible

    return 'N/A'

<<<<<<< HEAD
# returns a lst of tuple 
=======
>>>>>>> ef801acd69708f53f23d9cb099d8321301dd087e
def scrapper(url_lst):
    lst = []
    for url in url_lst:
        # url = 'https://' + url
        print('testing: ', url, '---------------------------')
        if 'blog' in url.split('/')[-1].lower(): # if blog is already there, e.g., www.innocentdrinks.co.uk/blog
<<<<<<< HEAD
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
            links = get_links('', response)
            res_lst = find_words(links)
=======
            res = url
>>>>>>> ef801acd69708f53f23d9cb099d8321301dd087e
        else:
            try: res = check_url(url)
            except Exception as e:
                res = 'error'
                print(e)
        lst.append(res)
    return lst

def main():
    company_lst = df_creation('test.csv')
    print(company_lst)
    res_lst = scrapper(company_lst)
    print(res_lst)
    make_csv('test.csv', res_lst)
    print('done')

main()




<<<<<<< HEAD
=======

>>>>>>> ef801acd69708f53f23d9cb099d8321301dd087e
