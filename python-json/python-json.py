import json

# Reading json content from .json file and converting into dictionary
f = open('sample.json').read()
dictionary = json.loads(f)
print(dictionary['name'])

# Converting dictionary to .json file ,
# Check new_json.json file to check content
json_string = json.dumps(dictionary , indent = 4)
f = open('new_json.json' , 'w')
f.write(json_string)
f.close()

##############################################################################################