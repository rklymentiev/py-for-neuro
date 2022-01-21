my_string = "P@#yn26at^&i5ve"

# set the initial values for the counter
word_characters_count = 0
digits_count = 0
symbols_count = 0

# iterate over the string
for val in my_string:
    if val.isalpha():   # check if a word character ('a', 'b', 'c')
        word_characters_count += 1
    elif val.isdigit(): # check if a digit (1, 2, 3)
         digits_count += 1
    else:               # the rest are symbols ('%', '@', '+')
        symbols_count += 1

# add resulting values to a dictionary
counts = {
    "Word Characters": word_characters_count,
    "Digits": digits_count,
    "Symbols": symbols_count
    }
print(counts)
