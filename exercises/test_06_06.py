def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert round(t_score, 2) == -2.36, "Check your t score."
    assert round(p_val, 2) == 0.01, "Check your p value."
    assert round(result["p-val"][0], 2) == 0.01, "P-value in ttest function is not correct"

    __msg__.good("Well done!")
