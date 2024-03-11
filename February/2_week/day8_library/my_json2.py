import json
data = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(data)
print(json_string)

json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(data)


