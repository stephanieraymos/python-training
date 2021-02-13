import json

# Opening json file
f = open('data.json',)

# Returns json object as dictionary
data = json.load(f)

# Iterating through the json list
for i in data['data']:
    print(i)

# Closing file
f.close()