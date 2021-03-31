def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert round(lower_bound, 3) == 0.942, "Check your lower bound calculations"
    assert round(upper_bound, 3) == 1.456, "Check your upper bound calculations"
    assert outliers_df.shape == (19, 12), "Shape of the DF with outliers doesn't match"

    __msg__.good("Well done!")
