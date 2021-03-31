def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert ("dashed" in __solution__) | ('--' in __solution__), 'Did you specify the dashed line?'
    assert (".mean()" in __solution__) | ('np.mean' in __solution__), \
    'Did you take the average of radius and/or texture?'

    __msg__.good("Well done!")
