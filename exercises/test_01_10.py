def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert max(v) < v_thresh, "Did you use the threshold value to reset the potential value?"
    assert min(v) == v_reset, "Did you use reset value to reset potential values?"
    assert round(sum(v)) == -57438, "Resulting v list doesn't match the solution."

    __msg__.good("Well done!")
