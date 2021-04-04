def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "heatmap" in __solution__, 'Did you call the heatmap function?'
    assert len(selected_columns) == 10, 'Did you include only the columns with average values in a list selected_columns?'
    assert corr_matrix.shape == (10,10), "Did you filter out the DataFrame before calling corr function?"

    __msg__.good("Well done!")
