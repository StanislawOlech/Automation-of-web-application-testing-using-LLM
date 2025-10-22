import random
from requirements.basic_requirements import *
from requirements.complex_requirements import *

# TODO Check if global list of objects is legal and won't result in ownership issues
all_text_box_req = [MinLengthRequirement(),
                    ContainsNumberRequirement(),
                    StartFromCapitalLetter(),
                    IsInTheList(),
                    ContainsLetter(),
                    ContainsSpecialChar(),
                    DigitsSumToOver(),
                    NegatedRequiment(MinLengthRequirement()),
                    NegatedRequiment(ContainsNumberRequirement()),
                    NegatedRequiment(StartFromCapitalLetter()),
                    NegatedRequiment(IsInTheList()),
                    NegatedRequiment(ContainsLetter()),
                    NegatedRequiment(ContainsSpecialChar()),
                    NegatedRequiment(DigitsSumToOver())]

all_button_req   = [ButtonALL(),
                    ButtonANY(),
                    ButtonAlwaysTrue(),
                    NegatedRequiment(ButtonALL()),
                    NegatedRequiment(ButtonANY()),
                    NegatedRequiment(ButtonAlwaysTrue())]


def get_random_requiment(is_button, task_difficulty=0.25):
    """
    Generate a random requirement for a button or text box.

    Parameters
    ----------
    is_button : bool
        Indicates whether the element is a button or a text box.
    task_difficulty : float, optional
        A float between 0 and 1 indicating the probability of generating a nested
        requirement.

    Returns
    -------
    Requirement
        The generated requirement.
    """
    if is_button:
        return(random.choice(all_button_req))

    if task_difficulty > random.uniform(0, 1):
        # TODO make that the requiments are not contradicting each other
        return(NestedRequiment(random.choice(all_text_box_req),
                               random.choice(all_text_box_req)))

    return(random.choice(all_text_box_req))
