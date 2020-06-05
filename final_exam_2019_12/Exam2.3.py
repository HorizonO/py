import requests
import re
html = requests.get("http://exercise.kingname.info/exercise_requests_get.html").content.decode()
title = re.search('title>(.*?)<',html,re.S).group(1)
content_list = re.findall('<p>(.*?)<',html,re.S)
content_str = '\n'.join(content_list)
print(f'title:{title}')
print(f'页面内容:\n{content_str}')
