def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert dof == 12, "Check the cross table. Do you have 4x5 (or 5x4) table?"
    assert round(chisq_stat) == 23, "chisq_stat is not correct"
    assert alpha == 0.05, "Did you set up the correct value of alpha?"
    assert round(threshold) == 16, "Check you threshold value"

    __msg__.good("Well done!")
