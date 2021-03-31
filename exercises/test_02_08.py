def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert height_var == None, 'Does your function check the type?'
    assert "assert" in __solution__, "Did you use assert statement?"
    assert "type(df)" in __solution__.replace(" ", ""), \
    "Do you check the type of degrees of freedom?"

    __msg__.good("Well done!")
