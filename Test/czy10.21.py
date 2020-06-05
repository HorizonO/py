from bs4 import BeautifulSoup
import requests
html = requests.get("http://exercise.kingname.info/exercise_bs_1.html").content.decode()
soup = BeautifulSoup(html,'lxml')
info_2 = soup.find(class_ = 'test')
print(f'使用find方法，返回的对象类型为:{type(info_2)}')
print(info_2.string)