from whichCMS import make_req
from cms_functions.wordpress import *
from cms_functions.drupal import *
from cms_functions.joomla import *

#use json_store to make a request and store it in that variable
#get_cms to get the cms used from json 
json_store = make_req('techcrunch.com')
get_cms = json_store["result"]["name"]

#function to determine which cms and what function to use
def which_cms(cms):

    if cms == "WordPress":
        return wordpress_func()
    if cms == "Drupal":  
        return drupal_func()
    if cms == "Joomla": 
        return joomla_func()
    return print("Invalid")

#test CMS
# print(json_store)
# print(get_cms)
which_cms(get_cms)

