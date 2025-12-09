# Automation-of-web-application-testing-using-LLM

The goal of this project is to harness the power of Large Language Models (LLMs) to generate test data for the evaluation of web applications. To simplify the problem, some assumptions and simplifications have been made. The target website was reduced to a series of buttons and text boxes, each having different requirements. The ultimate goal is to evaluate various LLM models and prompts in order to maximize the test coverage achieved by the AI model.


To perform this evaluation, two separate websites were generated: one without any errors, and another containing incorrect requirements. The number of errors depends on the badness level of the website. We recognize three types of errors:

- The requirement is always True,

- The requirement is always False,

- The requirement produces a mismatch from the correct answer.


This project was completed as part of the Model-Based and Test-Driven Development course in the Cyber-Physical Systems major within the Automatic Control and Robotics program at the AGH University of Krakow.


## Usage:


1. Create a Google AI Studio account

    Go to [Google AI Studio](https://aistudio.google.com/) and generate your own API key.

2. Save Your API Key

    You’ll need to create a secret.py file in your project’s root directory and store your API key inside it.


    Option 1 - Using PowerShell (Windows)
    ```powershell
    Set-Content -Path .\secret.py -Value 'api_key = "<YOUR_API_KEY_HERE>"'
    ```

    Option 2 – Manually (Any OS)

    Create a file named "secret.py" and add the following line:
    ```python
    api_key = "<YOUR_API_KEY_HERE>"
    ```
3. Run the Application
    ```powershell
    python main.py
    ```

### [Optional] Website Visualization

To visualize and test the website, run:

```powershell
python visualize_website.py
```


### [Optional] Test of Website Declared In JSON File

To test a specific website, you need to define a .json file similar to the following:

```json
{
    "elements": [
        {
            "type":        "textbox",
            "name":        "Username",
            "requirement": "IsInTheList",
            "negated":      true,
            "list":        ["admin", "user", "guest"]
        },
        ...
    ]
}
```

Then run:

```powershell
python test_specific_website.py --json_file "<YOUR_JSON_PATH_HERE>"'
```

Unfortunately, for now, nested requirements are not parsed correctly.


## Website requirements

In our simplified model, each website consists of between one and five elements. Each element is randomly assigned to be either a text box or a button (with a 50/50 probability).

Each element has an associated logical requirement, which can range from very simple (e.g., “always true”) to more complex conditions involving nested sub-requirements (see <em>Objects requirements</em> chapter). An element is considered satisfied if its defined requirement is met.


During evaluation, the website first checks whether each used element satisfies its requirement. It then verifies whether each unused element is also in a valid state. Currently, this verification occurs once in sequence across all elements, which may lead to edge cases — for example, requirements dependent on the satisfaction of previous elements or their negations.

For a website to pass the test, the overall output (i.e., the satisfaction state of all elements) must match that of the error-free website. A mismatch indicates that some element (button or text box) behaves incorrectly — for example, a text field accepting any password, a valid password being rejected, or a form allowing incomplete or incorrect data submission.



## Objects requirements

Each text box element can be associated with one or more of the following logical requirements:

1. Minimum length – The input must contain at least a specified number of characters.
(Default and currently the only active value: 5 characters.)

2. Contains a number – The input must include at least one numeric digit (0–9).

3. Starts with a capital letter – The input must begin with an uppercase alphabetic character (A–Z).

4. Matches allowed values – The input must exactly match one of the predefined allowed strings.
(Default and currently active values: ["Admin", "user", "test"].)

5. Contains a letter – The input must include at least one alphabetic character (A–Z or a–z).

6. Contains a special character – The input must include at least one non-alphanumeric character (e.g., !, #, $, %).

7. Digit sum threshold – The sum of all digits in the input must exceed a specified threshold.
(Default and currently active value: 5.)



Button elements can have one of the following logical requirements:

1. All previous text box conditions must be satisfied.
2. At least one of the previous text box conditions must be satisfied.
3. Always satisfied.



Additional Notes

- Each requirement have a reversed version, meaning the logical negation of the original condition is applied.

- Depending on the task_difficulty parameter (used in requirements.get_requirements), the system may generate nested or double requirements, where two conditions are combined (e.g., both must hold, or one negated, etc.) to increase complexity.