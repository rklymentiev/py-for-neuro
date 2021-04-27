def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert window == 150, "Did you chose the right window size?"
    assert h1_data["sta"].shape == (150, ), "Shape of the STA array is not correct."
    assert round(h1_data["sta"][0], 5) == -0.2129, "STA values are not correct."

    __msg__.good("Well done!")
