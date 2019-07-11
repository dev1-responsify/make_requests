from bs4 import BeautifulSoup
import requests
import lxml.html
import requests
import pandas as pd
from io import StringIO

# make a csv file
def make_csv(csv_file, lst):
    df = pd.read_csv(csv_file)
    df['result'] = lst
    df.to_csv('output.csv')

def df_creation(fileString):
    # temp = StringIO(fileString)
    df = pd.read_csv(fileString)
    return df['Root_Domain'].to_list()

# checks if url has blogs in the url
def check_url(url):
    print('in url: ', url)
    url1 = url + "/blog"
    url2 = url + '/tag/blog'
    url3 = url + '/blogs'
    try:
        requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
    except Exception as e:
        print(e)
        return 'N/A' # timeout or error so return N/A since site not accessible
    response = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code == 200: return url1
    response2 = requests.get(url2,  headers={'User-Agent': 'Mozilla/5.0'})
    if response2.status_code == 200: return url2
    response3 = requests.get(url3, headers={'User-Agent': 'Mozilla/5.0'})
    if response3.status_code == 200: return url3

    # if link is already the blog- check title to see if blog in name
    response4 = BeautifulSoup(requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text, 'html.parser')
    for i in response4.find_all("title"):
        if 'blog' in i.text.lower(): return url

    return 'N/A'

def scrapper(url_lst):
    lst = []

    for url in url_lst:
        url = 'https://' + url
        print('testing: ', url, '---------------------------')
        if 'blog' in url.split('/')[-1].lower(): # if blog is already there, e.g., www.innocentdrinks.co.uk/blog
            res = url
        else:
            try: res = check_url(url)
            except Exception as e:
                res = 'error'
                print(e)
        lst.append(res)
    return lst

def main():
    company_lst = df_creation('top500Domains.csv')
    print(company_lst)
    res_lst = scrapper(company_lst)
    print(res_lst)
    make_csv('top500Domains.csv', res_lst)
    print('done')

main()





