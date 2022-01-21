def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert parietal_df.shape == (532, 5), 'Did you filter only observation from parietal region?'
    assert "to_excel" in __solution__, 'Did you save resulting DataFrame as an Excel file?'

    __msg__.good("Well done!")
