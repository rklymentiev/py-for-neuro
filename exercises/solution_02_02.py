fibonacci_series = [0, 1]  # first two values of series

while len(fibonacci_series) < 10:  # condition for the length
    # add the new value
    fibonacci_series.append(sum(fibonacci_series[-2:]))

print(fibonacci_series)
