def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert int(F_stat) == 38, "F statistic from scipy package is not correct"
    assert int(result['F'][0]) == 38, "F statistic from pingouin package is not correct"

    __msg__.good("Well done!")
