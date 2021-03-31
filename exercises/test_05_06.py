def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert frmi['parietal'].shape == (532, 5), "Did you select only parietal part for the frmi['parietal']?"
    assert frmi['frontal'].shape == (532, 5), "Did you select only parietal part for the frmi['frontal']?"

    __msg__.good("Well done!")
