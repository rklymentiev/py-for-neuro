def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert first_author_name == dataset_description["Authors"][0]["Name"],\
    'That is not the authors name from the original dictionary'
    assert "first_author_name = output" in __solution__,\
    'Did you just typed the name in?'

    __msg__.good("Well done!")
