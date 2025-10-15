import numpy as np
import random

def test_website(website, test_data, treshold=0.1):
    correct_results = np.zeros(len(test_data))
    results         = np.zeros(len(test_data))

    for i, test in enumerate(test_data):
        correct_results[i] = website.use(test)

        results[i] = correct_results[i] if random.uniform(0, 1) > treshold else not correct_results[i]

    # TODO implement aggregation of results and metrics calculation
    pass