import os

# get the current working directory and save it to a variable
cwd = os.getcwd()
print(f"Initial CWD: {cwd}")

path_to_data = 'exercises/data'
# extend the current path with "path_to_data" part
new_cwd = os.path.join(cwd, path_to_data)
# change the CWD to new_cwd
os.chdir(new_cwd)
print(f"Changing CWD to {new_cwd}")

# get the file names of a CWD
fnames = os.listdir()

# calculate how many CSV files are there in CWD
n_csv = 0
for file_name in fnames:
    if file_name.endswith(".csv"):
        n_csv += 1

print(f"There are {n_csv} CSV files in {new_cwd} directory.")
