import json

mydata = '''
{"a":"1",
"b":"2",
"c":"3"
}
'''
data = json.loads(mydata)
print(data["a"])