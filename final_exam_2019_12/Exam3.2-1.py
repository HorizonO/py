import requests
import lxml.html
import re
#1)
html = requests.get("https://www.kanunu8.com/book3/8249/").content.decode('gb18030')
list = re.findall('><a href="(.*?)">(.*?)（(.*?)）</a></td>',html)#获得网址和章节的列表并返回
print(list)


#2)

def get_article(html):
    """
    获取每一章的正文并返回章节名和正文。
    :param html: 正文源代码
    :return: 章节名，正文
    """
    chapter_name = re.search('size="4">(.*?)<', html, re.S).group(1)
    text_block = re.search('<p>(.*?)</p>', html, re.S).group(1)
    text_block = text_block.replace('&nbsp;&nbsp;&nbsp;&nbsp;', '')
    text_block = text_block.replace('&quot;', '')
    text_block = text_block.replace('<br />', '')
    return chapter_name, text_block
get_article(html)