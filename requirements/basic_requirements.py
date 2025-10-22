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
        return f"more than {self.min_length} characters long."


class ContainsNumberRequirement(Requirement):
    def is_met(self, conditions, input):
        return any(char.isdigit() for char in input)

    def __str__(self):
        return "composed of numeric character."


class StartFromCapitalLetter(Requirement):
    def is_met(self, conditions, input):
        return input[0].isupper() if input else False

    def __str__(self):
        return "starting with a capital letter."


class IsInTheList(Requirement):
    def __init__(self, allowed_list=None):
        if allowed_list is None:
            allowed_list = ["Admin", "user", "test"]
        self.allowed_list = allowed_list

    def is_met(self, conditions, input):
        return input in self.allowed_list

    def __str__(self):
        return f"in the list: {self.allowed_list}."


class ContainsLetter(Requirement):
    def is_met(self, conditions, input):
        return any(char.isalpha() for char in input)

    def __str__(self):
        return "composed of a letter."


class ContainsSpecialChar(Requirement):
    def is_met(self, conditions, input):
        return any(not char.isalnum() for char in input)

    def __str__(self):
        return "composed of a special character."


class DigitsSumToOver(Requirement):
    def __init__(self, threshold=5):
        self.threshold = threshold

    def is_met(self, conditions, input):
        digits = [int(char) for char in input if char.isdigit()]
        return sum(digits) > self.threshold

    def __str__(self):
        return f"the sum of digits is over {self.threshold}."


# Button requirements

class ButtonALL(Requirement):
    def is_met(self, conditions, input):
        return all(conditions)  # TODO check if empty

    def __str__(self):
        return "enabled if all previous conditions are met."


class ButtonANY(Requirement):
    def is_met(self, conditions, input):
        return any(conditions) # TODO check if empty

    def __str__(self):
        return "enabled if at least one previous condition is met."


class ButtonAlwaysTrue(Requirement):
    def is_met(self, conditions, input):
        return True

    def __str__(self):
        return "true."