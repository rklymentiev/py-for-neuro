my_string = "P@#yn26at^&i5ve"

# start the counter
word_characters_count = ___  # like 'a', 'b', 'c'
digits_count = ___           # like '1', '4', '9'
symbols_count = ___          # like '%', '@', '+'

# iterate over the string
for ___ in ____:
    if ____:   # check if a word character
        word_characters_count = ____
    elif ____: # check if a digit
         digits_count = ___
    else:      # the rest are symbols
        symbols_count = ___

# add resulted values to a dictionary
counts = {
    "Word Characters": ___,
    "Digits": ___,
    "Symbols": ___
    }
print(counts)
