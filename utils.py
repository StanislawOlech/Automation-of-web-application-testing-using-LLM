from requirements.basic_requirements   import *
from requirements.complex_requirements import *

# TODO: add descriptions

def load_specification(file_path):
    with open(file_path, 'r') as file:
        spec = file.read()
    return spec


def make_requirement(req_name, element) -> Requirement:
    req = None

    if req_name == "MinLengthRequirement":
        req = MinLengthRequirement(element.get("value", 5)) # TODO It looks as if it always 5
    elif req_name == "ContainsNumberRequirement":
        req = ContainsNumberRequirement()
    elif req_name == "StartFromCapitalLetter":
        req = StartFromCapitalLetter()
    elif req_name == "IsInTheList":
        req = IsInTheList(element.get("list", []))
    elif req_name == "ContainsLetter":
        req = ContainsLetter()
    elif req_name == "ContainsSpecialChar":
        req = ContainsSpecialChar()
    elif req_name == "DigitsSumToOver":
        req = DigitsSumToOver(element.get("value", 5))
    elif req_name == "ButtonALL":
        req = ButtonALL()
    elif req_name == "ButtonANY":
        req = ButtonANY()
    elif req_name == "ButtonAlwaysTrue":
        req = ButtonAlwaysTrue()
    else:
        raise ValueError(f"Unknown requirement: {req_name}")

    if element.get("negated", False):
        req = NegatedRequirement(req)

    return req


def parse_elements(data):
    result = []

    for el in data.get("elements", []):
        is_complex = el.get("complex", False)

        req_obj = None

        if is_complex:
            complex_elements = el.get("complex", [])

            if len(complex_elements) < 2:
                raise ValueError("Complex requirement must have at least 2 elements")

            # Creating individual requirements
            complex_requirements = [
                make_requirement(comp_el["requirement"], comp_el)
                for comp_el in complex_elements
            ]

            # Combining to nested requirements
            req_obj = complex_requirements[0]
            for req in complex_requirements[1:]:
                req_obj = NestedRequirement(req_obj, req)

        else:
            req_obj = make_requirement(el["requirement"], el)



        is_button = (el.get("type") == "button")

        result.append((is_button, req_obj))

    return result


def progress_bar(current, total, bar_length=20):
    fraction = current / total

    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '

    ending = '\n' if current == total else '\r'

    print(f'Progress: [{arrow}{padding}] {int(fraction*100)}%', end=ending)