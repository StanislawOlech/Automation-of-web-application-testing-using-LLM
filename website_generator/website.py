import random
from requirements import *

class Website:
    # TODO fix the comments
    def __init__(self, spec, badness=0):
        # it should contain buttons and text boxes as per the spec
        # gets a list of touples (bool if_is_button, an class: requirement)
        # the order of buttons and text boxes should be the same as in the spec
        # conditions is a list of bools indicating if previous buttons/text boxes were used successfully

        self.objects = spec
        self.conditions = [False] * len(spec) # initially all conditions are False
        self.toggled    = [False] * len(spec) # to track button states
        self.seeds      = [random.randint(1, 3) * (random.uniform(0, 1) < badness) for _ in spec]

    def use(self, test_data):
        # it should use the text boxes and buttons based on the test data

        for index, input in test_data:
            result = self.objects[index][1].is_met(conditions=self.conditions, input=input)

            match self.seeds[index]:
                case 1:
                    result = not result
                case 2:
                    result = False
                case 3:
                    result = True

            self.conditions[index] = result

        for index, (is_button, requiment) in enumerate(self.objects):
            # May get affected by computation order but it is website feature
            if self.toggled[index]:
                continue
            result = self.objects[index][1].is_met(conditions=self.conditions, input="")

            match self.seeds[index]:
                case 1:
                    result = not result
                case 2:
                    result = False
                case 3:
                    result = True

            self.conditions[index] = result

        return self.conditions