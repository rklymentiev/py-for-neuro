def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert round(p_x25, 3) == 0.516, "P(X>=25) is not correct."
    assert round(p_x18, 3) == 0.024, "P(X=18) is not correct."
    assert len(x) == 66, "Did you include all the observations (from 0 to 65) in array x?"

    __msg__.good("Well done!")
