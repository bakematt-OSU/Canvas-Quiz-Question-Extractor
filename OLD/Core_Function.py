# ---------------------------------------------------
# QUIZ UTILITIES FOR LOADING, SAVING, AND ANALYSIS
# ---------------------------------------------------

import os
import json
from typing import List
from quiz_models import Quiz

QUIZ_ATTEMPT_FOLDER = "quiz_attempts"

os.makedirs(QUIZ_ATTEMPT_FOLDER, exist_ok=True)

def save_quiz_attempt(quiz: Quiz, attempt_id: str):
    """SAVE A QUIZ ATTEMPT TO DISK AS JSON."""
    output_path = os.path.join(QUIZ_ATTEMPT_FOLDER, f"{attempt_id}.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(quiz.to_dict(), f, indent=2)

def load_quiz_attempt(attempt_id: str) -> Quiz:
    """LOAD A SAVED QUIZ ATTEMPT FROM DISK."""
    input_path = os.path.join(QUIZ_ATTEMPT_FOLDER, f"{attempt_id}.json")
    with open(input_path, "r", encoding="utf-8") as f:
        return Quiz.from_dict(json.load(f))

def load_all_quiz_attempts() -> List[Quiz]:
    """LOAD ALL SAVED QUIZ ATTEMPTS FROM DISK."""
    quizzes = []
    for filename in os.listdir(QUIZ_ATTEMPT_FOLDER):
        if filename.endswith(".json"):
            with open(os.path.join(QUIZ_ATTEMPT_FOLDER, filename), "r", encoding="utf-8") as f:
                quizzes.append(Quiz.from_dict(json.load(f)))
    return quizzes

def extract_unique_questions_with_correct_answers(quizzes: List[Quiz]):
    """BUILD A LIST OF UNIQUE QUESTIONS WITH CORRECT ANSWERS FROM MULTIPLE QUIZ ATTEMPTS."""
    seen = {}
    for quiz in quizzes:
        for q in quiz.questions:
            key = q.text.strip().lower()
            if key not in seen:
                correct_opts = [opt for opt in q.options if opt.is_selected and q.points_awarded == q.points_possible]
                if correct_opts:
                    q.options = correct_opts  # Keep only the correct ones
                seen[key] = q
    return list(seen.values())
