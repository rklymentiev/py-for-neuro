# string with outcomes
outcomes =  ['malignant', 'malignant', 'benign', 'malignant',
             'malignant', 'benign', 'benign', 'benign']

# saving the string to txt file
with open('outcome.txt', mode='w') as file:
    for val in outcomes:       # write each value from the list at a new line
        file.write(val + "\n") # adding "\n" creates a new line in a file

# import the file as a string
___ ___('___', mode=___) as ___:
    outcomes_str = ___.___()

# import the file as a list
with open('outcome.txt', mode='r') as file:
    outcomes_list = file.readlines()

print("Imported string:")
print(outcomes_str)

print("Imported list:")
print(outcomes_list)

outcomes_list = list(___) # clean the values in a list
print("\nFixed list:")
print(outcomes_list)
