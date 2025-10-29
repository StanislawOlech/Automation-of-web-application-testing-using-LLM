import random
from requirements.get_requirements import get_random_requirement

def generate_specification():
    """
    Generate a random list of specification requirements of a website.

    Parameters
    ----------


    Returns
    -------
    list of tuple[bool, Requirement]
        Specification list of tuples (is_button, requirement)

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
        is_button = random.choice([True, False])
        requirement = get_random_requirement(is_button)
        spec.append((is_button, requirement))

    return spec