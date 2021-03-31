def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert type(good_trials) == list, "Didn't you forget to convert to list?"
    assert len(good_trials) == 7, "Didn't you forget to filter out bad trials?"

    __msg__.good("Well done!")
