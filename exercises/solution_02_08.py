def variance(input_list, df=1):

    assert (type(df) == int) & (df >= 0), \
    "Degrees of freedom should be a positive integer or 0"
    # get the list of booleans that were a result of checking
    # if value from a list is either int or float
    is_type_numeric = map(lambda x: type(x) in [int, float], input_list)
    # if the sum of that list doesn't equal the length of an input list
    # that means, that one of more objects were not numeric
    assert sum(is_type_numeric) == len(input_list), \
    "Some of the values in the list are not numeric"

    N = len(input_list)                # calculate the sample size
    x_bar = sum(input_list) / N        # calculate the average value

    numerator = []                     # empty list with the values from the numerator
    for x in input_list:               # iterate over all values in the given list
        numerator.append((x-x_bar)**2) # subtract average value from x,
                                       # square it, and add to the numerator list
    return sum(numerator) / (N-df)     # return the sum of the numerator divided by (N - df)


try:
    participants_height = [167, 185, 179, 191, 178, 180, 175, 188, "170"]
    height_var = variance(input_list=participants_height)
except:
    height_var = None

print(height_var)
