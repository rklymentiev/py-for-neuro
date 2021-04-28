def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert fpz_index == 1, "Check FPz electrode index."
    assert N == 50001, "Number of observations N is not correct."
    assert fc_np.shape == (50001,), "Did you select the electrode before applying FFT?"
    assert fc_sp.shape == (50001,), "Did you select the electrode before applying FFT?"

    __msg__.good("Well done!")
