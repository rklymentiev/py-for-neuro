def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    b_corr = np.load("exercises/data/b.npy")
    assert sum(b == b_corr) == 2, 'Did you use formula from above?'

    __msg__.good("Well done!")
