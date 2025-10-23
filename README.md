# Automation-of-web-application-testing-using-LLM

The goal of this project is to harness the power of Large Language Models (LLMs) to generate test data for the evaluation of web applications. To simplify the problem, some assumptions and simplifications have been made. The target website was reduced to a series of buttons and text boxes, each having different requirements. The ultimate goal is to evaluate various LLM models and prompts in order to maximize the test coverage achieved by the AI model.


To perform this evaluation, two separate websites were generated: one without any errors, and another containing incorrect requirements. The number of errors depends on the badness level of the website. We recognize three types of errors:

- The requirement is always True,

- The requirement is always False, and

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