___ variance(___):           # function with one input argument for a list object
    N = ___                  # calculate the sample size
    x_bar = ___              # calculate the average value

    numerator = ___          # empty list with the values from the numerator
    for x in ___:            # iterate over all values in the given list
        numerator.___(___)   # subtract average value from x,
                             # square it, and add to the numerator list
    ___ ___ / ___            # return the sum of the numerator divided by N


participants_height = [167, 185, 179, 191, 178, 180, 175, 188, 170]
height_var = variance(___)
print(height_var)
