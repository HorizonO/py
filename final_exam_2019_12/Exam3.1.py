# -*- coding: utf-8 -*-
import requests
import lxml.html
from lxml import etree
from bs4 import BeautifulSoup
import re
import csv


person_dict = []
txt = open('Exam3.1.txt','r',encoding='UTF-8')
source = txt.read()
# print(source)
selector = lxml.html.fromstring(source)
person_list = selector.xpath('//ul[@class="p_author"]')
# person_list = selector.xpath('//div[@class="l_post j_l_post l_post_bright"]/div')
text = selector.xpath('//div[@class="d_post_content_main"]/div')
print(text)
for t in text:
    show_text = t.xpath('div[@class="d_post_content j_d_post_content  clearfix"]/div')
    print(show_text)
    # aa = '>(.*?)<'
    # print(re.match(r'>(.*?)<',show_text))

# for person in person_list:
#     # username = person.xpath('/div[@class="d_author"]/ul[@class="p_author"]/li[@class="d_name"]/a/text()')
#     username = person.xpath('li[@class="d_name"]/a/text()')
#     # show_text = person.xpath('div[@class="d_post_content j_d_post_content  clearfix"]')
#     # show_time=person.xpath('div[@class="core_reply j_lzl_wrapper"]/div[@class="core_reply_tail "]/ul[@class="p_tail"]/li/span/text()')
#     print(username)
    # print(show_time)
    # print(show_text)

# print(person_list)
# xpath
# dict_list = []
# person_list = selector.xpath('//li[@class="d_name"]/a/text()')
# for person in person_list:
#     show_name = person.xpath()
#     show_post = person.xpath()
#     show_time = person.xpath()
#     print("用户名是："+show_name)
#
#     person_dict={'show_name':show_name[0] if show_name else ''
#                  'show_post:'show_post[1] if show_post else ''}
#     dict_list.append(person_list)
# print(dict_list)
# with open('result.csv', 'w', encoding='utf-8') as f:
#     writer = csv.DictWriter(f, fieldnames=['show_name'])
#     writer.writeheader()
#     writer.writerows(dict_list)
#soup
# soup = BeautifulSoup(source, 'lxml')
#
# useful = soup.find(class_='p_author_name j_user_card')
# print(useful)
# s = '<a alog-group="p_author" class="p_author_name j_user_card" data-field='{"un":"MRJ_\u8c4c\u8c46","id":"tb.1.37951aa1.hyDEcQEe8ahOIk7vNBBSnw"}' href="/home/main?un=MRJ_%E8%B1%8C%E8%B1%86&amp;ie=utf-8&amp;id=tb.1.37951aa1.hyDEcQEe8ahOIk7vNBBSnw&amp;fr=pb&amp;ie=utf-8" target="_blank">MRJ_豌豆</a>'
# ss = re.search('>(.*?)</a',s)
# print(ss)
# content = re.search('>(.*?)</a',useful)

# print(content)
