import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint


# Make a request to the WHATCMS server
def make_req(url):
    # API_key variable that is used for whatCMS. Change if necessary
    api_key = '23dfc4228f6e198adf4a4f7a05817d7b'
    api_url_base = 'https://api.diffbot.com/v3/article?token=' + api_key   + '&url=' + url
    response = requests.get(api_url_base)
    soup = BeautifulSoup(response.text, 'html.parser')
    #Print response if successful and error if unsuccessful
    if response:
        print('Success!')
        x = response.json()
        
        return response.json()
       
    else:
        print('An error has occurred.')


# returns the number of words in a texts
def count_words(text):
    lst = text.split()
    return len(lst)

# returns the information from the obj in the api
# returns error if info not there
def get_info(res, obj):
    try: return obj['objects'][0][res]
    except: return 'object does not exist'

# get all the links on that page 
# task: determine which links are blogs 
# challenge: some blogs don't have /blog in href ex: blogs in responsify.com/blog
def get_links(obj):
    raw_data = get_info('html', obj)
    res_lst = raw_data.split('<')
    result = set()
    for i in res_lst:
        if 'href' in i: # strips quotes, etc. and add link to set
            try: result.add((i.split('=')[1]).replace('"', '').rstrip('/>'))
            except: pass
    return result

        
def main():
    obj = make_req('https://www.responsify.com/blog/')
    words = count_words(obj['objects'][0]['text'])
    print('title:', get_info('title', obj))
    print('author:', get_info('author', obj))
    links = get_links(obj)
    for i in links: print(i)
    # print('num words:', words)

main()
