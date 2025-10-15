import numpy as np
import random

def test_website(good_website, bad_website, test_data, treshold=0.5):
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