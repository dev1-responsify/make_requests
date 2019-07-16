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
        
        # pprint(x)
        # print(x['title'])
        # print(x['objects'][0]['author'])
        # print(x['objects'][0]['images'])
        # print(x['objects'][0]['title'])
        # print(x['objects'][0]['text'])
        return response.json()
       
    else:
        print('An error has occurred.')

def count_words(text):
    lst = text.split()
    return len(lst)

def main():
    obj = make_req('https://www.responsify.com/convert-meaning/')
    words = count_words(obj['objects'][0]['text'])
    print('title:', obj['objects'][0]['title'])
    print('author:', obj['objects'][0]['author'])
    print('num words:', words)

main()
