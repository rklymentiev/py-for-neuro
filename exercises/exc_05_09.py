import os

# get the current working directory and save it to a variable
cwd = ___.___()
print(f"Initial CWD: {cwd}")

path_to_data = 'exercises/data'
# extend the current path with "path_to_data" part
new_cwd = os.path.___(___, path_to_data)
# change the CWD to new_cwd
___.___(new_cwd)
print(f"Changing CWD to {new_cwd}")

# get the file names of a CWD
fnames = ___.___()

# calculate how many CSV files are there in CWD
n_csv = ___

print(f"There are {___} CSV files in {___} directory.")
