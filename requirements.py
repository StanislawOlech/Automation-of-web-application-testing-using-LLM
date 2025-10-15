from abc import ABC, abstractmethod

class Requirement(ABC):
    @abstractmethod
    def is_met(self, conditions, input):
        ...


# Text box requirements

class MinLengthRequirement(Requirement):
    def __init__(self, min_length=5):
        self.min_length = min_length

    def is_met(self, conditions, input):
        return len(input) >= self.min_length

class MaxLengthRequirement(Requirement):
    def __init__(self, max_length=10):
        self.max_length = max_length

    def is_met(self, conditions, input):
        return len(input) <= self.max_length

class ContainsNumberRequirement(Requirement):
    def is_met(self, conditions, input):
        return any(char.isdigit() for char in input)

class StartFromCapitalLetter(Requirement):
    def is_met(self, conditions, input):
        return input[0].isupper() if input else False

class IsNotInTheList(Requirement):
    def __init__(self, forbidden_list=None):
        if forbidden_list is None:
            forbidden_list = ["admin", "user", "test"]
        self.forbidden_list = forbidden_list

    def is_met(self, conditions, input):
        return input not in self.forbidden_list

class IsInTheList(Requirement):
    def __init__(self, name_list=None):
        if name_list is None:
            name_list = ["admin", "user", "test"]
        self.name_list = name_list

    def is_met(self, conditions, input):
        return input in self.name_list

class AbsenceOfLetters(Requirement):
    def is_met(self, conditions, input):
        return all(not char.isalpha() for char in input)

class ContainsLetter(Requirement):
    def is_met(self, conditions, input):
        return any(char.isalpha() for char in input)

# Special character requirement
# Numbers sum requirement


# Button requirements

class ButtonALL(Requirement):
    def is_met(self, conditions, input):
        return all(conditions)

class ButtonANY(Requirement):
    def is_met(self, conditions, input):
        return any(conditions)

# Conditions should be a list of all previous tested buttons and text boxes
# Input should be the string for text boxes and bool for buttons