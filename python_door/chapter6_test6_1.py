dict = {
    'first_name':'H',
    'last_name':'orizon',
    'age':20,
    'city':'GZ',
}
print(dict)

#6-2
nums = {'a':1,'b':2,'c':3}
if nums['a'] == 1:
    print('y')
if nums['b'] == 2:
    print('y')
print(nums)

#6-5
rivers = {'cj':'CHINA','hh':'CHINA','s':'HK'}
for river in rivers.keys():
    for city in rivers.values():
        print('')
    print('The '+river.title()+' runs through '+city)