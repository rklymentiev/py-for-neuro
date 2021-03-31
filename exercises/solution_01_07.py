five_to_three = "GGATCC"
# replace to small case since to prevent replacing newly replaced values
three_to_five = five_to_three.replace('G', 'c').replace('A', 't').replace('T', 'a').replace('C', 'g')
# upper method and slicing could be applied in a previous line
# but I splitted it for better visual representation
three_to_five = three_to_five.upper()[::-1]
is_palindrome = five_to_three == three_to_five
print(is_palindrome)
