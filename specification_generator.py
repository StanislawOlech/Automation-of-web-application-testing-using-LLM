import random
from requirements import *

def generate_specification():
    """
    Generate a random list of specification requirements of a website.

    Parameters
    ----------


    Returns
    -------
    list of tuple[bool, Requirement]
        Specification list of touples (is_button, requirement)

    Description
    -----------
    This function randomly creates between 1 and 5 specification entries.
    Each entry represents a tuple describing either a button-related
    requirement or a general text/content requirement. The specific
    requirement type is chosen at random from a predefined set of
    requirement classes imported from `requirements`.
    """

    num_of_objects   = random.randint(1, 5)

    spec = []

    for _ in range(num_of_objects):
        if_is_button = random.choice([True, False])
        if if_is_button:
            requirement = random.choice([ButtonALL(),
                                        ButtonANY(),
                                        ButtonAlwaysTrue(),
                                        ButtonAlwaysFalse()])
        else:
            requirement = random.choice([MinLengthRequirement(),
                                         MaxLengthRequirement(),
                                         ContainsNumberRequirement(),
                                         StartFromCapitalLetter(),
                                         IsNotInTheList(),
                                         IsInTheList(),
                                         ContainsLetter()])
        spec.append((if_is_button, requirement))

    return spec