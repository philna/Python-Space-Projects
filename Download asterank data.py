"""""

This script connects to the Asterank API which provides access to the NASA Small Body Database
along with some modifications to estimate monetary value and other financial/feasiblity metrics

August 11, 2017

"""

import requests
import json


#Request results from Asterank API - query for all results with limit value set to 100
response = requests.get("http://www.asterank.com/api/asterank?query={}&limit=1000")

#Decode response as json list (not a dictionary for this API)
data = response.json()

# OPTIONAL - Add exception handling here in case response.json fails - look for ValueError:  No JSON object could be decode

#This code enumerates data column names such as e - eccentricity, name - asteroid name
for i, item in enumerate(data[3],0):
    print(i, item)


#Iterate through Aterank JSON and extract data - temporary - use map and joing to format and then export as .csv file

for i in range(len(data)):
    print(
        data[i]['e'],
        data[i]['a'],
        data[i]['name'],
        data[i]['producer'],
        data[i]['full_name'],
        data[i]['class'],
        data[i]['producer'],
        data[i]['GM'],
        data[i]['spec'],
        data[i]['closeness'],
        data[i]['price'],
        data[i]['score'],
        data[i]['neo']
          )






"""

print(data[0]['e'])
print(data[0]['a'])

# Get the response data as a python object.
data = response.json()

print(response)
print(type(data))

print(data[5]["e"])


for i, v in data.items():
    print(i,v)



for i, item in enumerate(data[3],0):
    print(i, item)

for i in data:
    print(i)


data = json.load(response,
                 cls=None,
                 object_hook=None,
                 parse_float=None,
                 parse_int=None,
                 parse_constant=None,
                 object_pairs_hook=None, **kw)
                 )


print(type(data))

"""





