import random
from requirements.basic_requirements import *

def apply_error(result, type_of_error):
    """
    Apply a specified type of error to a boolean result.


    Parameters
    ----------
    result : bool
        The original boolean result to potentially modify.
    type_of_error : int
        An integer indicating the type of error to apply:
        - 1: Invert the result (True becomes False, and vice versa).
        - 2: Always return False.
        - 3: Always return True.
        - Any other value: No error; return the original result.


    Returns
    -------
    bool
        The modified boolean result after applying the specified error.
    """

    match type_of_error:
        case 1: # invert
            return not result
        case 2: # always false
            return False
        case 3: # always true
            return True
        case _: # no error
            return result


class Website:
    def __init__(self, spec, badness=0):
        """
        Initialize the Website with a given specification and badness level.

        Parameters
        ----------
        spec : list of tuple[bool, Requirement]
            Specification list of tuples (is_button, requirement)
        badness : float, optional
            A float between 0 and 1 indicating the probability of introducing errors
            in the website's behavior. Default is 0 (no errors).

        Returns
        -------
        None


        Description
        -----------
        Initialize the website with the provided specification. The specification
        defines the elements (buttons and text boxes) and their associated requirements.
        The badness parameter controls the likelihood of errors occurring in the
        website's functionality, simulating potential faults or unexpected behaviors.
        """

        self.objects = spec
        self.conditions = [False] * len(spec) # initially all conditions are False
        self.toggled    = [False] * len(spec) # to track button states
        self.errors     = [random.randint(1, 3) * (random.uniform(0, 1) < badness) for _ in spec]

    def use(self, test_data):
        """
        Simulate using the website with a series of test inputs.

        Parameters
        ----------
        test_data : list of tuple[int, str or None]
            A list of moves, where each move is a tuple containing:
            - index of the button/text box to interact with (int)
            - input value for text boxes (str) or None for buttons.

        Returns
        -------
        list of bool
            A list of boolean values indicating whether each requirement is met
            after processing the test inputs.

        Description
        -----------
        This method processes a series of test inputs, simulating interactions
        with the website's buttons and text boxes. It evaluates whether the
        requirements associated with each element are met, taking into account
        any errors introduced based on the website's badness level.
        """

        for index, input in test_data:
            result = self.objects[index][1].is_met(conditions=self.conditions[:index], input=input)

            result = apply_error(result, self.errors[index])

            self.conditions[index] = result


        # evaluation of not toggled buttons/text boxes
        # WARNING: May lead to different results based on computation order
        for index, (is_button, requiment) in enumerate(self.objects):
            if self.toggled[index]:
                continue
            result = self.objects[index][1].is_met(conditions=self.conditions, input="")

            result = apply_error(result, self.errors[index])

            self.conditions[index] = result

        return self.conditions