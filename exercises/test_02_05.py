def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert ("df=1" in __solution__) | ("df = 1" in __solution__), \
    "Did you add the df argument with 1 as a default value?"
    assert round(height_var, 4) != 55.9506, "Did you subtract df in the denominator?"
    assert round(height_var, 4) == 62.9444, "Hmm.. Something is wrong with your function."

    __msg__.good("Well done!")
