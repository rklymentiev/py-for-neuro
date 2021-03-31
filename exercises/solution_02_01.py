my_string = "P@#yn26at^&i5ve"

# start the counter
word_characters_count = 0    # like 'a', 'b', 'c'
digits_count = 0             # like '1', '4', '9'
symbols_count = 0            # like '%', '@', '+'

# iterate over the string
for val in my_string:
    if val.isalpha():   # check if a word character
        word_characters_count += 1
    elif val.isdigit(): # check if a digit
         digits_count += 1
    else:               # the rest are symbols
        symbols_count += 1

# add resulted values to a dictionary
counts = {
    "Word Characters": word_characters_count,
    "Digits": digits_count,
    "Symbols": symbols_count
    }
print(counts)
