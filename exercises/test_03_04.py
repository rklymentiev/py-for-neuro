def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert sorted(agg_df.columns) == ['Count', 'nWBV_median'], 'Have you renamed the columns?'
    assert sorted(agg_df.index) == [0.0, 0.5, 1.0, 2.0], "Have you grouped by CDR column?"
    assert agg_df.loc[0.0, "nWBV_median"] == 0.773, 'Did you use the median function?'

    __msg__.good("Well done!")
