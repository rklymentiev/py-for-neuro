def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert avg_ses1 == avg_ses2, 'Average values are not equal'
    assert round(avg_ses1,3) == 2.331, 'Did you filter the data properly?'

    __msg__.good("Well done!")
