from abc import ABC, abstractmethod

class Requirement(ABC):
    @abstractmethod
    def is_met(self, conditions, input):
        """
        Check if the requirement is met based on conditions of other elements and current input.


        Parameters
        ----------
        conditions : list of bool
            List of boolean values indicating if previous buttons/text boxes were used successfully.
        input: str or None
            The current input to evaluate. For text boxes, this is a string input.


        Returns
        -------
        bool
            True if the requirement is met, False otherwise.

        Description
        -----------
        This method should be implemented by subclasses to define specific requirement logic. In general,
        it evaluates whether the current input satisfies the requirement, potentially considering the
        state of previous elements as indicated by the `conditions` list.
        """
        ...

    @abstractmethod
    def __str__(self):
        """
        Return a human-readable description of the requirement. Needed for generating prompts.
        """
        ...


# Text box requirements

class MinLengthRequirement(Requirement):
    def __init__(self, min_length=5):
        self.min_length = min_length

    def is_met(self, conditions, input):
        return len(input) >= self.min_length

    def __str__(self):
        return f"The text is at least {self.min_length} characters long."


class MaxLengthRequirement(Requirement):
    def __init__(self, max_length=10):
        self.max_length = max_length

    def is_met(self, conditions, input):
        return len(input) <= self.max_length

    def __str__(self):
        return f"The text is at most {self.max_length} characters long."


class ContainsNumberRequirement(Requirement):
    def is_met(self, conditions, input):
        return any(char.isdigit() for char in input)

    def __str__(self):
        return "The text contains at least one numeric character."


class StartFromCapitalLetter(Requirement):
    def is_met(self, conditions, input):
        return input[0].isupper() if input else False

    def __str__(self):
        return "The text starts with a capital letter."


class IsNotInTheList(Requirement):
    def __init__(self, forbidden_list=None):
        if forbidden_list is None:
            forbidden_list = ["admin", "user", "test"]
        self.forbidden_list = forbidden_list

    def is_met(self, conditions, input):
        return input not in self.forbidden_list

    def __str__(self):
        return f"The text is not in the forbidden list: {self.forbidden_list}."


class IsInTheList(Requirement):
    def __init__(self, allowed_list=None):
        if allowed_list is None:
            allowed_list = ["admin", "user", "test"]
        self.allowed_list = allowed_list

    def is_met(self, conditions, input):
        return input in self.allowed_list

    def __str__(self):
        return f"The text is in the allowed list: {self.allowed_list}."


class AbsenceOfLetters(Requirement):
    def is_met(self, conditions, input):
        return all(not char.isalpha() for char in input)

    def __str__(self):
        return "The text contains no alphabetic characters."


class ContainsLetter(Requirement):
    def is_met(self, conditions, input):
        return any(char.isalpha() for char in input)

    def __str__(self):
        return "The text contains at least one alphabetic character."


# TODO add more requirements
# Special character requirement
# Numbers sum requirement


# Button requirements

class ButtonALL(Requirement):
    def is_met(self, conditions, input):
        return all(conditions)  # TODO check if empty

    def __str__(self):
        return "All previous conditions must be met."


class ButtonANY(Requirement):
    def is_met(self, conditions, input):
        return any(conditions) # TODO check if empty

    def __str__(self):
        return "At least one previous condition must be met."


class ButtonAlwaysTrue(Requirement):
    def is_met(self, conditions, input):
        return True

    def __str__(self):
        return "This button always True."


class ButtonAlwaysFalse(Requirement):
    def is_met(self, conditions, input):
        return False

    def __str__(self):
        return "This button always False."