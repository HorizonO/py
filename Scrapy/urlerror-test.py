from urllib.parse import urlparse
from urllib import  request,error
import re
import json
import requests
# try:
#     response = request.urlopen("https://horizono.github.io")
# except error.HTTPError as e:
#     print(e.code)
#     print(e.reason)
#     print(e.headers)
# else:
#     print('request successfully')
# result = urlparse('https://horizono.github.io')
# print(type(result),result)
data = {'name':'germey','age':'22'}
r = requests.post('https://horizono.github.io/post',data=data)
print(r.text)