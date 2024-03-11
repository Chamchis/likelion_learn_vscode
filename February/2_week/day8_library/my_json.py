import json
data = {'name':'John','age':21,'country':'United States'}
json_string = json.dumps(data)
print(data)
print(json_string)
print(type(json_string))
data = json.loads(json_string)
print(data)
print(type(data))
with open('data_file_json','w') as f:
    json.dump(data,f)
with open('data_file_json','r') as f:
    data_get = json.load(f)
print(data_get)
print(json.dumps(data, indent=4))