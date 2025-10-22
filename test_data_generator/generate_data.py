import random

def generate_test_data(spec):
    """
    Generate test data based on the provided website specification.


    Parameters
    ----------
    spec : list of tuple[bool, Requirement]
        Specification list of touples (is_button, requirement)


    Returns
    -------
    list of tuple[int, str or None]
        A list of moves, where each move is a tuple containing:
        - index of the button/text box to interact with (int)
        - input value for text boxes (str) or None for buttons.
    """
    # TODO Do it with LLM instead of this placeholder

    test_data = []
    num_of_test  = 5 # TODO chose a suitable number
    num_of_moves = 3 # TODO chose a suitable number

    for _ in range(num_of_test):
        move = []
        for _ in range(num_of_moves):
            index = random.randint(0, len(spec)-1)
            if spec[index][0]: # button
                input = None # the move of the button is understood as clicking it
            else: # text box
                input = random.choice(["test", "Test1", "12345", "Admin", "hello", "HELLO", "user123", "no_numbers", "123456", "A1b2C3", "short", "thisisaverylonginput"])
            move.append((index, input))
        test_data.append(move)

    return test_data