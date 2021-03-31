def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert counts['Word Characters'] == 8, "Something is wrong with the Word Characters count"
    assert counts['Digits'] == 3, "Something is wrong with the Digits count"
    assert counts['Symbols'] == 4, "Something is wrong with the Symbols count"

    __msg__.good("Well done!")
