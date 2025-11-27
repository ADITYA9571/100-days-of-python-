# beautiful soup--bs4
# refer to site jsonplaceholder
# get, put, post, etc/...requests:http for hummans
import requests
from bs4 import BeautifulSoup
# response = requests.get("https://jsonplaceholder.typicode.com/")
# print(response.text)
url = "https://jsonplaceholder.typicode.com/posts"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
for heading in soup.find_All("h2"):
    print(heading.text)
# data = { 
#     "title":'foo',
#     "body":'bar',
#     "userId":1,
# }
# headers = {
#     'content-type':'application/json; charset = UTF-8'
# }
# response = requests.post(url, headers = headers, json = data )
# print(response.text)