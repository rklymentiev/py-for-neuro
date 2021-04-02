accuracy_scores = {
    'id1': 0.27, 'id2': 0.75, 'id3': 0.61, 'id4': 0.05, 'id5': 0.4,
    'id6': 0.67, 'id7': 0.69, 'id8': 0.52, 'id9': 0.7, 'id10': 0.3
    }
# store the top 3 values from the dictionary as a list
max_accs = sorted(accuracy_scores.values(), reverse=True)[:3]
# create an empty list that will hold ids of participants with the highes accuracy
max_ids = []                             # create an empty list
for key in accuracy_scores.keys():       # iterate over all keys in the dictionary
    if accuracy_scores[key] in max_accs: # check if the value of this key is in top 3
        max_ids.append(key)              # if so, append the list

print(max_ids)
