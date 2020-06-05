from bs4 import BeautifulSoup
import requests
import re

html = requests.get('http://exercise.kingname.info/exercise_bs_1.html').content.decode()

soup = BeautifulSoup(html, 'lxml')

content = soup.find_all(class_=re.compile('iam'))
for each in content:
    print(each.string)

