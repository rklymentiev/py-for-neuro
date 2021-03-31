import requests

# URL of an API request
URL = 'http://api.open-notify.org/astros.json'
# GET method
response = requests.get(URL)
# check the status code
print(f"Status code: {response.status_code}")
# convert result to the dictionary
output = response.json()

# get all the names in a list
names = []
for person in output["people"]:
    names.append(person["name"])

print(names)
