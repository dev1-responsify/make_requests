import json
import requests


# Make a request to the WHATCMS server
def make_req(url):
    # API_key variable that is used for whatCMS. Change if necessary
    api_key = '2435acd0fea8d22f1444b63291eef03ed58779b4d57699c5f6c520cf634cc6b1777253'
    api_url_base = 'https://whatcms.org/APIEndpoint/Detect?key=' + api_key   + '&url=' + url
    response = requests.get(api_url_base)

    #Print response if successful and error if unsuccessful
    if response:
        print('Success!')
        return response.json()
       
    else:
        print('An error has occurred.')


