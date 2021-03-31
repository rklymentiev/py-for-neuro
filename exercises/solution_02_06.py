accuracy_scores = {
    'id1': 0.27, 'id2': 0.75, 'id3': 0.61, 'id4': 0.05, 'id5': 0.4,
    'id6': 0.67, 'id7': 0.69, 'id8': 0.52, 'id9': 0.7, 'id10': 0.3
    }

good_ids = list(filter(lambda x: accuracy_scores[x] > 0.6, accuracy_scores.keys()))
print(good_ids)
