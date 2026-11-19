
# AI Student Task Planner

## Project Overview

The AI Student Task Planner is a Python-based project that uses an AI model to generate structured JSON study plans based on user input.

The project ensures that the generated information follows a predefined schema and returns validated, typed data.

## Objective

The main objective is to generate reliable JSON output using an AI model, validate the generated data, reject invalid responses, and retry when validation fails.

## Technologies Used

- Python
- OpenAI API
- Pydantic
- JSON

## Project Features

1. Generates study plans using an AI model.
2. Defines a predefined JSON schema.
3. Validates AI-generated output using Pydantic.
4. Rejects invalid data.
5. Implements a retry and repair mechanism.
6. Returns structured and typed JSON data.

## Project Structure

AI_Student_Task_Planner/
- main.py
- requirements.txt
- README.md

## Installation

Install the required Python libraries:

pip install -r requirements.txt

Configure your OpenAI API key as an environment variable:

OPENAI_API_KEY

## How to Run

1. Open the project folder.
2. Open main.py using Python IDLE.
3. Run the program by pressing F5.
4. Enter your study task.
5. The AI generates a structured study plan.
6. The program validates the output and displays the final JSON.

## Example Input

Prepare for my Python examination in 5 days.

## Example JSON Output

{
    "task_title": "Python Exam Preparation",
    "subject": "Python",
    "priority": "High",
    "deadline": "5 days",
    "study_hours": 3,
    "action_steps": [
        "Revise Python basics",
        "Practice Python programs",
        "Solve examination questions"
    ]
}

## Validation and Error Handling

The project uses Pydantic to validate the generated output against the predefined schema.

If the output fails validation, the program provides corrective feedback and retries up to three times.

If valid data cannot be generated, the program reports an error instead of returning invalid data.

## Conclusion

This project demonstrates how AI-generated information can be converted into reliable structured JSON output using schema definition, data validation, and retry mechanisms.
