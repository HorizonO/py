from urllib.request import urlopen
url='http://www.bing.com'
response = urlopen(url)
print(response.closed)
with response:
    print(response.status)
    print(type(response))
    print(response.geturl())
print(response.closed)