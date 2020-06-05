from bs4 import BeautifulSoup
import requests
import re

html = requests.get('http://exercise.kingname.info/exercise_bs_1.html').content.decode()

soup = BeautifulSoup(html, 'lxml')

useful = soup.find(class_='useful')
all_content = useful.find_all('li')
for li in all_content:
    print(li.string)
