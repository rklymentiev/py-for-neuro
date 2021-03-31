trial_ids = ["001", "002", "003", "004", "005",
             "006", "007", "008", "009", "010"]
bad_trials = ["004", "006", "007"]

good_trials = list(set(trial_ids) - set(bad_trials))
print(good_trials)
