def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert round(radius_mean_malignant,2) == 15.03, 'Average radius for the malignant cell is wrong'
    assert round(radius_mean_benign,2) == 11.37, 'Average radius for the benign cell is wrong'

    __msg__.good("Well done!")
