from bs4 import BeautifulSoup
import requests
from requests.models import iter_slices


url ='https://www.hbtbank.com/meet-our-mortgage-bankers'
r = requests.get(url).text

soup = BeautifulSoup(r,'lxml')
video = soup.find_all('div',class_='col-6')

for i in video:
    name = ''
    title = ''
    number = ''

    try:
        name = i.find('a').text
        # print(name)
    except:
        pass

    try:
        title = i.find('p').text
        
    except:
        pass


# for title in soup.find_all('span',{'id':'video-title'}):
#     print(title)