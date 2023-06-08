import json
f=open('data4.json')
data=json.load(f)
with open('data5.json', 'w') as outfile:
    json.dump(data,outfile,indent=4)