from abc import ABC, abstractmethod

class Requirement(ABC):
    @abstractmethod
    def is_met(self, conditions, input):
        ...

# Conditions should be a list of all previous tested buttons and text boxes
# Input should be the string for text boxes and bool for buttons