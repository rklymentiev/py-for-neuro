def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert len(good_ids) == 5, "Do you have five IDs in a list?"
    assert sorted(good_ids) == ['id2', 'id3', 'id6', 'id7', 'id9'], "Your selected IDs don't match with the solution."

    __msg__.good("Well done!")
