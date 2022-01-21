accuracy_scores = {
    'id1': 0.2665, 'id2': 0.7523, 'id3': 0.6123, 'id4': 0.053, 'id5': 0.389,
    'id6': 0.6732, 'id7': 0.692, 'id8': 0.5184, 'id9': 0.743, 'id10': 0.3111
    }

for (key, value) in accuracy_scores.items():
    print(f"Accuracy for subject {key} is {value:.2f}.")

# alternative
# for key in accuracy_scores.keys():
#     print(f"Accuracy for subject {key} is {accuracy_scores[key]:.2f}.")
