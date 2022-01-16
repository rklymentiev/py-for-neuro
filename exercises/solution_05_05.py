import json
import pprint

dataset_description = {
    "Name": "Our cool data set",
    "Authors": [
        {
            "Name": "Bob",
            "Institution": "X"
        },
        {
            "Name": "Ben",
            "Institution": "Y"
        }
    ],
    "Version": "0.0.1"
}

# write JSON file
with open(file="dataset_description.json", mode="w") as file:
    json.dump(obj=dataset_description, fp=file)

# read JSON file
with open(file="dataset_description.json", mode="r") as file:
    output = json.load(fp=file)

pprint.pprint(output)

# get the name of the first author
first_author_name = output["Authors"][0]["Name"]
print(f"\nFirst author is {first_author_name}")
