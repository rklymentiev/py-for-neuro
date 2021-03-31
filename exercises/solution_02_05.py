def variance(input_list, df=1):        # function with one input argument for a list object
    N = len(input_list)                # calculate the sample size
    x_bar = sum(input_list) / N        # calculate the average value

    numerator = []                     # empty list with the values from the numerator
    for x in input_list:               # iterate over all values in the given list
        numerator.append((x-x_bar)**2) # subtract average value from x,
                                       # square it, and add to the numerator list
    return sum(numerator) / (N-df)     # return the sum of the numerator divided by (N - df)


participants_height = [167, 185, 179, 191, 178, 180, 175, 188, 170]
height_var = variance(input_list=participants_height)
print(height_var)
