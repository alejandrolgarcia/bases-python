# Python JSON

import json

# some JSON
x = '{ "name": "Tony Stark", "age": 30, "city": "Los Angeles" }'

# parse x
y = json.loads(x)

# the result is a Python dictionary
print(y["name"])        # Tony Stark

# Convert from Python to JSON
# a python object (dict)
info = { 
    "name": "Tony Stark", 
    "age": 30, 
    "city": "Los Angeles" 
}

# convert into JSON
y = json.dumps(x)

# the result is a Json string
print(y)
