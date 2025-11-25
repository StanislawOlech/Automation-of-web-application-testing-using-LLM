from requirements.basic_requirements   import *
from requirements.complex_requirements import *

# TODO: add descriptions

def load_specification(file_path):
    with open(file_path, 'r') as file:
        spec = file.read()
    return spec


def make_requirement(req_name, element) -> Requirement:
    # TODO implement all requirements
    if req_name == "IsInTheList":
        return IsInTheList(element.get("list", []))
    elif req_name == "MinLengthRequirement":
        return MinLengthRequirement()
    elif req_name == "ContainsLetter":
        return ContainsLetter()
    elif req_name == "ButtonALL":
        return ButtonALL()
    else:
        raise ValueError(f"Unknown requirement: {req_name}")


def parse_elements(data):
    result = []

    for el in data.get("elements", []):
        req_obj = make_requirement(el["requirement"], el)

        if el.get("negated", False):
            req_obj = NegatedRequirement(req_obj)

        is_button = (el.get("type") == "button")

        result.append((is_button, req_obj))

    return result


def progress_bar(current, total, bar_length=20):
    fraction = current / total

    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '

    ending = '\n' if current == total else '\r'

    print(f'Progress: [{arrow}{padding}] {int(fraction*100)}%', end=ending)