import random
import ast
import re
from google import genai
try:
    from secret import api_key
except ImportError:
    raise FileNotFoundError("secret.py not found. Please create it and add your API key.")

if not api_key or api_key.startswith("<"):
    raise ValueError("API key not set. Please update secret.py with your Google AI Studio API key.")


def generate_prompt(spec, num_tests, num_moves, informed=True):
    """
    Generate prompt for data generation. Depending on the "informed_prompt" flag it
    will include requirements for prompt generation.


    Parameters
    ----------
    spec : list of tuple[bool, Requirement]
        Specification list of tuples (is_button, requirement)
    num_tests : int
        Number of test cases to generate.
    num_moves : int
        Number of moves per test case.
    informed_prompt : bool, optional
        Flag indicating whether to include requirements in the prompt.



    Returns
    -------
    str
        Generated prompt string.
    """

    prompt = "You are generating test cases for a website.\n\n"
    prompt += "Each UI element is described below:\n"
    for i, (is_button, requirement) in enumerate(spec):
        element_type = "Button" if is_button else "Text box"
        prompt += f"{i}. {element_type} — {requirement}\n" if informed else  f"{i}. {element_type}\n"
    prompt += (
        f"\nGenerate {num_tests} test cases. Each test case should contain {num_moves} moves.\n"
        "Each move should be a tuple of the form (index, input_value), where input_value is None for buttons.\n"
        "Output in valid Python list syntax, no explanations.\n"
    )
    return prompt


def generate_test_data(spec, informed_prompt=True, num_tests=5, num_moves=3):
    """
    Generate test data based on the provided website specification. Depending on the "informed_prompt" flag the prompt
    will include requirements for prompt generation.


    Parameters
    ----------
    spec : list of tuple[bool, Requirement]
        Specification list of tuples (is_button, requirement)
    informed_prompt : bool , optional
        Flag indicating whether to include requirements in the prompt.
    num_tests : int, optional
        Number of test cases to generate.
    num_moves : int, optional
        Number of moves per test case.


    Returns
    -------
    list of tuple[int, str or None]
        A list of moves, where each move is a tuple containing:
        - index of the button/text box to interact with (int)
        - input value for text boxes (str) or None for buttons.
    """

    prompt = generate_prompt(spec,
                             num_tests=num_tests,
                             num_moves=num_moves,
                             informed=informed_prompt)


    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    clean_text = re.sub(r',\s*([\]\)])', r'\1', response.text)
    clean_text = clean_text.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    clean_text = ''.join(ch for ch in clean_text if ord(ch) >= 32 or ch in '\n\t')
    clean_text = clean_text.replace('null', 'None')

    if clean_text.startswith("```python"):
        clean_text = clean_text[len("```python"):]
    if clean_text.endswith("```"):
        clean_text = clean_text[:-3]

    try:
        generated_data = ast.literal_eval(clean_text)
    except Exception as e:
        generated_data = generate_test_data(spec) # evil programming


    return generated_data