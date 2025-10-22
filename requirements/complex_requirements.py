from requirements.basic_requirements import *

class NestedRequiment(Requirement):
    def __init__(self, req1, req2):
        self.req1 = req1
        self.req2 = req2

    def is_met(self, conditions, input):
        return self.req1.is_met(conditions, input) and self.req2.is_met(conditions, input)

    def __str__(self):
        str_req1 = self.req1.__str__()[:-1]                                     # Removed from the end"."
        str_req2 = self.req2.__str__()[0].lower() + self.req2.__str__()[1:]     # Lowercase first letter

        return str_req1 + " and " + str_req2


class NegatedRequiment(Requirement):
    def __init__(self, req):
        self.req = req

    def is_met(self, conditions, input):
        return not self.req.is_met(conditions, input)

    def __str__(self):
        return "not " + self.req.__str__()