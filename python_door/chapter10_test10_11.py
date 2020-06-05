#coding=utf-8
import json
number = input("请输入你喜欢的数字：")
filename = 'number.json'
with open(filename,'w') as f_obj:
    json.dump(number,f_obj)
    print("这个数字已存储！")
