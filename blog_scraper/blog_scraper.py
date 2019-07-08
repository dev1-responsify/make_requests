from bs4 import BeautifulSoup
import requests
# from csv import writer

response = requests.get("https://www.techcrunch.com")

soup = BeautifulSoup(response.text, 'html.parser')  

# with open('posts.csv', 'w') as csv_file:
#     csv_writer = writer(csv_file)
#     head
# ers = ['Title', 'Link', 'Date']
#      csv_writer.writerow(headers)
posts = soup.find_all(class_="type-blogteaser-standard-headline text-center responsify-serif")



#link = soup.find_all('a')

links = [a.get('href') for a in soup.find_all('a', href=True)]
print(links)
    


blogpost = links[0]
blogrequest = requests.get(blogpost)
# print(blogrequest.text)

soup_two = BeautifulSoup(blogrequest.text, 'html.parser') 


if blogrequest.status_code == 200:
    print('Success!')
elif blog_request.status_code == 404:
    print('Not Found.')

word_count = soup_two.find_all('p')
store = ""
for n in word_count:
    print(n.get_text())
    store += n.get_text()

word = 'char count = '

print(word + str(len(store)))

    
