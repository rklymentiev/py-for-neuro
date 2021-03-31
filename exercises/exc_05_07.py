import requests

# URL of an API request
URL = ___
# GET method
response = requests.get(URL)
# check the status code
print(f"Status code: {response.status_code}")
# convert result to the dictionary
output = response.json()

# get all the names in a list
names = []
for person in ___:
    names.___(___)

print(names)
