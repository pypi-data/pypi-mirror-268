from promptflow.core import tool


@tool
def validate_inputs(question: str, answer: str, ground_truth: str):
    # Validate input parameters
    if (
        not (question and question.strip() and question != "None")
        or not (answer and answer.strip() and answer != "None")
        or not (ground_truth and ground_truth.strip() and ground_truth != "None")
    ):
        raise ValueError("'question', 'answer' and 'ground_truth' must be non-empty strings.")

    return True
