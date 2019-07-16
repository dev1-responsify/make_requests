from bs4 import BeautifulSoup
import requests
import lxml.html
import requests
import pandas as pd

# make a csv file
def make_csv(csv_file, lst):
    df = pd.read_csv(csv_file)
    df['result'] = lst
    df.to_csv('output.csv')

# checks if url has blogs in the url
def check_url(url):
    print('in url: ', url)
    url1 = url + "blog"
    url2 = url + 'tag/blog'
    url3 = url + 'blogs'
    try:
        response = requests.get(url1,  headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        if response.status_code == 200: return url1
    except: return None # timeout or error so return None since site not accessible
    response2 = requests.get(url2,  headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
    if response2.status_code == 200: return url2
    response3 = requests.get(url3, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
    if response3.status_code == 200: return url3

    # if link is already the blog- check title to see if blog in name
    response4 = BeautifulSoup(requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10).text, 'html.parser')
    for i in response4.find_all("title"):
        if 'blog' in i.text.lower(): return url

    # try:
    #     url4 = 'https://' + 'blogs.' + url.split("/")[-2] # https://blogs.random.com
    #     response4 = requests.get(url4, headers={'User-Agent': 'Mozilla/5.0'})
    #     if response4.status_code == 200: return url4
    # except: pass

    return None

def scrapper(url_lst):
    lst = []
    for url in url_lst:
        print('testing: ', url, '---------------------------')
        if 'html' in url.split('/')[-1].lower():
            print(url)
            res = None
        elif 'blog' in url.split('/')[-1].lower(): # if blog is already there, e.g., www.innocentdrinks.co.uk/blog
            res = url
        else:
            res = check_url(url)
        lst.append(res)
    return lst


# lst = ['https://www.doyouyoga.com/', 'https://www.reuters.com/', 'https://www.blogilates.com/', 'https://www.houzz.com/',
#        'https://www.100daysofrealfood.com/', 'https://inhabitat.com/', 'https://pando.com/', 'https://iso.500px.com/',
#        'https://www.innocentdrinks.co.uk/blog']
lst = ['http://www.datasciencecentral.com/', 'http://www.datatau.com/', 'https://www.kdnuggets.com/news/index.html',
       'https://www.reddit.com/r/datascience/', 'https://news.google.com/news/section?q=data%20science',
       'https://www.analyticsvidhya.com/blog/', 'https://www.datacamp.com/community/blog', 'http://chrisalbon.com/',
       'http://blog.yhat.com/', 'http://101.datascience.community/', 'https://datascience.nih.gov/blog',
       'https://blog.mailchimp.com/tag/data-science/', 'http://datascience.ibm.com/blog/',
       'https://datascience.berkeley.edu/blog/', 'http://cds.nyu.edu/news/',
       'http://compbio.ucsd.edu/outreach/data-science-blog/', 'http://blog.kaggle.com/category/data-science-news/',
       'https://dssg.uchicago.edu/blog/', 'https://www.codementor.io/data-science/tutorial',
       'http://datasciencedegree.wisconsin.edu/blog/']

# link = 'https://designformankind.com/blog/'
# soup =  BeautifulSoup(requests.get(link, headers={'User-Agent': 'Mozilla/5.0'}).text)
# print(soup.prettify())
x = scrapper(lst)
# x = check_url('https://iso.500px.com/')
print(x)







