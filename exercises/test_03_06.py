def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "unknown" in joined_table["diagnosis"].unique(), 'Did you replace and save the missing values?'
    assert "id" in joined_table.columns, 'Did you exclude the redundant ID column?'

    __msg__.good("Well done!")
