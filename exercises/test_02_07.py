def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert groups_cleaned[0] == 'control', 'Did you clean the groups list?'
    assert groups_cleaned[2] == 'treatment', 'Did you clean the groups list?'
    assert sorted(ids_trt) == ['id3', 'id5', 'id6', 'id7', 'id8'], "Your treatment IDs don't match with the solution."
    assert sorted(ids_ctl) == ['id1', 'id10', 'id2', 'id4', 'id9'], "Your control IDs don't match with the solution."

    __msg__.good("Well done!")
