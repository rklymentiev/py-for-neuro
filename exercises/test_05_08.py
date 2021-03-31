def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "69750516" in URL, "Did you add subject ID to the URL?"
    assert "quality=50" in response.url, "Did you set the 50% quality?"
    assert img.shape == (1250, 1250, 3), "Did you set the image size in parameters?"

    __msg__.good("Well done!")
