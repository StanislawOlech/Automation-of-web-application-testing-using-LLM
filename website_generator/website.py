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
        self.badness   = badness
        self.seed       = random.uniform(0, 1)

    def use(self, test_data):
        # it should use the text boxes and buttons based on the test data

        for index, input in test_data:
            result = self.objects[index][1].is_met(conditions=self.conditions, input=input)

            if self.badness >= self.seed % (index+1):  # TODO check if that seed usage is ok
                result = not result # TODO code allways true and allways false

            self.conditions[index] = result

        for index, (is_button, requiment) in enumerate(self.objects):
            # May get affected by computation order but it is website feature
            if self.toggled[index]:
                continue
            result = self.objects[index][1].is_met(conditions=self.conditions, input="")

            if self.badness >= self.seed % (index+1):
                result = not result

            self.conditions[index] = result

        return self.conditions