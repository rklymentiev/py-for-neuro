def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert len(fibonacci_series) == 10, "Length of the list is not 10."
    assert sum(fibonacci_series) == 88, "Something wrong with your series."

    __msg__.good("Well done!")
