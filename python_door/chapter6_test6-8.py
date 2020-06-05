onedict = {'a':1,'b':2}
twodict = {'c':3,'d':4}
three = {
    'two':twodict,
    'one':{'a':1,'b':2},
}
print(three)

#6-11
cities = {
    'GuangDong':{'country':'GZ','population':'one million','fact':'hot'},
    'JiangMen':{'country':'XH','population':'ten thousands','fact':'warm'}
}
for city in cities:
    print(cities.keys())