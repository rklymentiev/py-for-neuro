def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert c1_loc.argmax() == 26, "c1_loc doesn't match the solution."
    assert c1_data.shape == (1, 1001), "Did you slice the eeg['data'] array correctly?"
    assert (max_v == c1_data.max()) | (max_v == c1_data[0,:].max()), \
        "Maximum value result doesn't match the solution."
    assert (min_v == c1_data.min()) | (min_v == c1_data[0,:].min()), \
        "Minimum value result doesn't match the solution."
    assert (mean_v == c1_data.mean()) | (mean_v == c1_data[0,:].mean()), \
        "Mean value result doesn't match the solution."
    assert (t_max_v == np.where(c1_data[0, :] == max_v)) | (t_max_v == np.where(c1_data == max_v)), \
        "Index of the maximum value result doesn't agree with the solution."
    assert (t_min_v == np.where(c1_data[0, :] == min_v)) | (t_min_v == np.where(c1_data == min_v)), \
        "Index of the minumum value result doesn't match the solution."

    __msg__.good("Well done!")
