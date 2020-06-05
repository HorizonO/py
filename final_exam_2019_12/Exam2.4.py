import requests
import lxml.html
source = requests.get('http://tieba.baidu.com/f?ie=utf-8&kw=%E9%99%88%E9%81%93%E6%98%8E&fr=search').content
selector = lxml.html.fromstring(source)
post_title_list = selector.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/text()')
for post_title in post_title_list:
    print(post_title)