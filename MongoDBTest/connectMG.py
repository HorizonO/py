import pymongo
client = pymongo.MongoClient(host='localhost',port=27017)
db=client.test
s=db.students
stu1={
    'name':'李四',
    'sex':'女',
    'class':'17计科1班'
}
stu2={
    'name':'王五',
    'sex':'男',
    'class':'17计科2班'
}
result=s.insert([stu1,stu2])
print(result)
