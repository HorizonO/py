#coding = utf-8
import json
filename = "number.json"
with open(filename) as f_obj:
    number = json.load(f_obj)
    print("I konw your favorite number! It's " + number)
