def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert len(nwbv_estimation.keys()) == 3, "Does you dictionary have three keys?"
    assert len(nwbv_estimation[0].keys()) == 2, "Did you add mean and CI values as a nested dictinary?"
    assert nwbv_estimation[0]['mean'] == 0.7692, "Values in a dictinary are not correct"

    __msg__.good("Well done!")
