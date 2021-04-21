import ___ as pd
import matplotlib.___ as plt
from sklearn import tree

# import the file
dementia_df = pd.___("exercises/data/oasis_cross-sectional.csv")

# drop redundant columns
model_data = dementia_df.___(columns=["ID", "Hand", "Delay"])
model_data.dropna(___) # drop missing values
# create a new binary column, 1 if subject has dementia, 0 otherwise
model_data["dementia"] = model_data["CDR"].___
# drop CDR column
model_data.drop(___)
# convert gender column to numerical, 1 if female, 0 otherwise
model_data["M/F"] = model_data["M/F"].___

X = ___ # dataframe with features only
y = ___ # column with the dementia status

# build the model
model = tree.DecisionTreeClassifier(
    criterion='entropy',
    max_depth=3)

# fit the data
model.fit(X, y)

plt.figure(figsize=(11, 7), facecolor="white")
tree.plot_tree(
    decision_tree=model,
    filled=True, # fill the cells according to the class
    feature_names=X.columns.tolist(),
    # use proportions of class occurrence instead of absolute values
    proportion=True,
    class_names=['No Dementia', 'Dementia'])
plt.show()
