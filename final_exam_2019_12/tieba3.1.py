import re
import csv

with open('Exam3.1.txt','r',encoding='UTF-8') as f:
    source = f.read()
result_list = []
#每一层的版块
every_floor = re.findall('l_post l_post_bright j_l_post clearfix  "(.*?)p_props_tail props_appraise_wrap',source,re.S)
# print(every_floor)

#分别获取评论，用户名，评论时间作测试
# reply = re.findall('d_post_content j_d_post_content  clearfix" style="display:;"(.*?)</div',source,re.S)
# print(reply)
# user_name = re.findall('=utf-8" target="_blank">(.*?)</a>',source,re.S)
# print(user_name)
# reply_time = re.findall('date&quot;:&quot;(.*?)&quot;,&quot;vote_',source,re.S)
# print(reply_time)
for each in every_floor:
    # print(each)
    result = {}
    result['username'] =  re.findall('target="_blank">(.*?)</a>',each,re.S)[0]          #获取用户名
    result['content'] = re.findall('style="display:;"> (.*?)</div><br>',each,re.S)[0].replace('            ', '')   #获取评论
    result['reply_time'] = re.findall('楼</span><span class="tail-info">(.*?)</span></div>',each,re.S)[0]            #获取发布时间
    result_list.append(result)
    print(result)
#获取用户名、发帖内容和发帖时间，并保存为Exam3_1.csv
with open('Exam3.1.csv', 'w', encoding='UTF-8') as f:
    writer = csv.DictWriter(f, fieldnames=['username', 'content', 'reply_time'])
    writer.writeheader()
    writer.writerows(result_list)
