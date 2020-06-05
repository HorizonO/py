import urllib.request
import time
import pymongo
from lxml import etree

#用urllib访问网页
#首先是get_page()部分
#要爬取的网页有十页
#发现第一页网址为https://movie.douban.com/top250?start=0&filter=
#第二页网址为https://movie.douban.com/top250?start=25&filter=
#只有start属性发生了改变，每次加25
#最后一页的网址为https://movie.douban.com/top250?start=225&filter=
#所以设定一个偏移量offset，获取网页的时候每次加25

def get_page(offset):
    response = urllib.request.urlopen('https://movie.douban.com/top250?start='+offset+'&filter=')
    #reponse 为 HTTPResposne 类的对象
    #常用 read()方法可以得到网页信息 调用status属性可以的到返回结果的状态码
    if response.status == 200:
        html = etree.HTML(response.read())
        #修正html文本，可以将缺少的部分补充完整，方便解析
        response = etree.tostring(html).decode('utf-8')
        #将修正的结果进行输出，输出类型为bytes类型，需要调用decode方法解码为str类型
        #print(type(response))
        return response
#下面是parse_page()部分,使用xpath选择器
def parse_page(response):
    responses = etree.fromstring(response)
    #转化为lxml.etree._Element类，其中有xpath()方法
    #print(type(responses))
    lists = responses.xpath('//*[@id="content"]/div/div[1]/ol//li')
    #提取所有的li节点
    for list in lists:
        ranking = ''.join(list.xpath('./div/div[1]/em/text()'))
        fable = ''.join(list.xpath('./div/div[1]/ol/li[1]/div/div[2]/div[2]/p[2]/span'))
        title = ''.join(list.xpath('./div/div[2]/div[1]/a/span[1]/text()'))
        grade = ''.join(list.xpath('./div/div[2]/div[2]/div/span[2]/text()'))
        comment_num = ''.join(list.xpath('./div/div[2]/div[2]/div/span[4]/text()'))
        #在相应的节点下输入/text()可以获取节点内的文字
        #取出来都发现是列表形式的，所以用一个''.join()方法转化为字符串
        yield {
            'ranking': ranking,#排名
            'fable' : fable,#名言
            'title': title,#名称
            'grade': grade,#豆瓣评分
            'comment_num':comment_num#评论人数
        }
        #yield作用相当于return,迭代一次yield就会返回yield后面的值，这里是以字典的形式返回信息

#save_to_mongodb()部分
def save_to_mongodb(results):
    client = pymongo.MongoClient(host='localhost',port=27017)
    #创建客户端
    db = client['douban_top250']
    #指定数据库
    collection = db["doubanmovies"]
    #指定集合
    for result in results:
        if collection.find_one({'title':result['title']}) is None:#如何没有相应的数据，储存
            collection.insert(result)
            print('储存成功'+str(result))

#最后设置一个循环
def main(offset):
    response = get_page(str(offset*25))
    results = parse_page(response)
    save_to_mongodb(results)
    time.sleep(3)

if __name__ == '__main__':
    for offset in range(0,10):
        main(offset)
