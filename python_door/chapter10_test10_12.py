import json
filename = 'numbers.json'
try:
    with open(filename) as f_obj:
        number = json.load(f_obj)
except FileNotFoundError:
    number = input("What is your favorite number?")
    with open(filename,'w') as f_obj:
        json.dump(number,f_obj)
        print("已存储")
else:
    print("I konw your favorite number! It's " + number)