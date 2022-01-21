def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert Qs.shape == (101, 3), "Shape of Qs array is not correct"
    assert sum(Qs[-1, :].round(3) == [0.212, 0.726, 0.467]) == 3, "Value function values don't match the solution."
    assert cum_rew[-1] == 64, "Cumulative reward doesn't match the solution."
    assert sum(counts == [20, 26, 54]) == 3, "Counts of chosen arms doesn't match the solution."

    __msg__.good("Well done!")
