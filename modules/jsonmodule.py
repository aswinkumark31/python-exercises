import json


# json object to python object -- python str

x = '{"name":"abc","age":23}'
print(type(x)) 
print(x)

y=json.loads(x)
print(y)
print(type(x))  


x = [1,2,3,4]
print(type(x))
y =json.dumps(x)
print(y)
print(type(y))

x=(1,2,3,4)
print(type(x))
y=json.dumps(x)
print(y)
print(type(y))

x='asdf'
y=json.dumps(x)
print(y)
print(type(y))

 