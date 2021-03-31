def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert condition == False, "Did you consider all the conditions?"
    assert "group == " in __solution__, "Did you consider the group condition?"
    assert "BMI >= 15" in __solution__, "Did you consider the BMI criteria?"
    assert "age > 40" in __solution__, "Did you consider the age criteria?"

    __msg__.good("Well done!")
