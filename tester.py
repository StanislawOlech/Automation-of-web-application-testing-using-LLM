def test_website(good_website, bad_website, test_data):
    """
    Test two websites against the same test data and return the accuracy of their
    responses.


    Parameters
    ----------
    good_website : Website
        A website instance that is expected to behave correctly.
    bad_website : Website
        A website instance that is expected to behave incorrectly.
    test_data : list of tuple[int, str or None]
        A list of moves, where each move is a tuple containing:
        - index of the button/text box to interact with (int)
        - input value for text boxes (str) or None for buttons.


    Returns
    -------
    float
        The accuracy of the bad website compared to the good website, calculated as
        the ratio of matching responses to total responses.


    Description
    -----------
    This function simulates the use of two websites (one good and one bad) with the
    same series of test inputs. It compares their responses to determine how often
    the bad website produces the same results as the good website, providing a measure
    of the test vectors coverage.
    """
    true  = 0
    false = 0

    for i, test in enumerate(test_data):
        correct_results = good_website.use(test)
        bad_results     = bad_website.use(test)

        if correct_results != bad_results:
            false += 1
        else:
            true += 1

    return true / (true + false)