import json 
f=open('data2.json')
data=json.load(f)
for i in data:
    print(len(i['variants']))