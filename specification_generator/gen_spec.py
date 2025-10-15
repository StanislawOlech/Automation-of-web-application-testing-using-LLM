import random
from requirements import *

def generate_specification():
    # should return a table of touples (bool if_is_button, an class: requirement)

    num_of_objects   = random.randint(1, 5)

    spec = []

    for _ in range(num_of_objects):
        if_is_button = random.choice([True, False])
        if if_is_button:
            requirement = random.choice([ButtonALL(),
                                        ButtonANY()])
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