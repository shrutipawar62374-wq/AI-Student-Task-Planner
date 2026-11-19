
import os
import json
from enum import Enum
from openai import OpenAI
from pydantic import BaseModel, Field, ValidationError


# ==========================================
# 1. CONNECT TO OPENAI
# ==========================================

client = OpenAI()


# ==========================================
# 2. DEFINE JSON SCHEMA
# ==========================================

class Priority(str, Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class StudyPlan(BaseModel):

    task_title: str = Field(min_length=3)
    subject: str = Field(min_length=2)
    priority: Priority
    deadline: str = Field(min_length=2)
    study_hours: int = Field(ge=1, le=12)
    action_steps: list[str] = Field(min_length=2, max_length=5)


# ==========================================
# 3. GENERATE STRUCTURED AI OUTPUT
# ==========================================

def generate_plan(user_task):

    error_message = ""

    for attempt in range(1, 4):

        try:

            print("\nAttempt:", attempt)

            response = client.chat.completions.parse(

                model="gpt-4o-mini",

                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an AI student task planner. "
                            "Generate a useful study plan. "
                            "Follow the given schema exactly. "
                            "Do not invent unrealistic study hours."
                        )
                    },

                    {
                        "role": "user",
                        "content": (
                            "Create a study plan for this task: "
                            + user_task
                            + "\n"
                            + error_message
                        )
                    }
                ],

                response_format=StudyPlan
            )

            result = response.choices[0].message

            if result.refusal:
                raise ValueError("AI refused the request.")

            if result.parsed is None:
                raise ValueError("AI returned no valid structured data.")

            # Additional validation
            validated_data = StudyPlan.model_validate(
                result.parsed.model_dump()
            )

            return validated_data

        except (ValidationError, ValueError) as error:

            print("Invalid output:", error)

            error_message = (
                "Your previous output failed validation. "
                "Correct the following problem: "
                + str(error)
            )

        except Exception as error:

            print("API or connection error:", error)
            raise

    raise RuntimeError(
        "Failed to generate valid output after 3 attempts."
    )


# ==========================================
# 4. DISPLAY FINAL JSON OUTPUT
# ==========================================

def display_plan(plan):

    print("\n====================================")
    print("       GENERATED STUDY PLAN")
    print("====================================")

    final_data = plan.model_dump(mode="json")

    print(json.dumps(final_data, indent=4))

    print("\n====================================")
    print("VALIDATION SUCCESSFUL")
    print("====================================")


# ==========================================
# 5. MAIN PROGRAM
# ==========================================

def main():

    print("====================================")
    print("       AI STUDENT TASK PLANNER")
    print("====================================")

    user_task = input("\nEnter your study task: ").strip()

    if not user_task:
        print("Error: Task cannot be empty.")
        return

    try:

        plan = generate_plan(user_task)

        display_plan(plan)

    except RuntimeError as error:

        print("\nProject failed:", error)

    except Exception as error:

        print("\nSomething went wrong:", error)


# ==========================================
# 6. RUN PROGRAM
# ==========================================

if __name__ == "__main__":
    main()



