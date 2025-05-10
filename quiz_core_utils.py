"""
QUIZ CORE UTILITIES MODULE

THIS MODULE HANDLES THE SAVING, LOADING, AND PROCESSING OF QUIZ ATTEMPT DATA.
IT SUPPORTS ORGANIZING QUIZ ATTEMPTS BY CLASS, RETRIEVING ATTEMPTS BY ID,
AND EXTRACTING UNIQUE QUESTIONS WITH ONLY CORRECT ANSWERS RETAINED.
"""

import os
import json
from typing import List
from quiz_models import Quiz

# DEFINE THE FOLDER WHERE QUIZ ATTEMPT FILES WILL BE STORED
QUIZ_ATTEMPT_FOLDER = "quiz_attempts"

# CREATE THE FOLDER IF IT DOES NOT ALREADY EXIST
os.makedirs(QUIZ_ATTEMPT_FOLDER, exist_ok=True)

def save_quiz_attempt(quiz: Quiz, attempt_id: str, class_name: str):
    """
    SAVE A QUIZ ATTEMPT TO A JSON FILE, NESTED UNDER THE CLASS NAME.

    ARGS:
        quiz (Quiz): THE QUIZ ATTEMPT TO BE SAVED
        attempt_id (str): UNIQUE IDENTIFIER TO NAME THE JSON FILE
        class_name (str): CLASS NAME TO NEST THE QUIZ UNDER

    RETURNS:
        NONE
    """
    # CONSTRUCT THE FULL OUTPUT PATH FOR THE JSON FILE
    output_path = os.path.join(QUIZ_ATTEMPT_FOLDER, f"{attempt_id}.json")

    # CREATE A SUBDIRECTORY FOR THE CLASS NAME
    class_folder = os.path.join(QUIZ_ATTEMPT_FOLDER, class_name)
    os.makedirs(class_folder, exist_ok=True)

    # DEFINE FULL OUTPUT PATH AS: quiz_attempts/ClassName/attempt_id.json
    output_path = os.path.join(class_folder, f"{attempt_id}.json")

    # STRUCTURE: Class -> Quiz -> Attempt
    data = {
        class_name: {
            quiz.title: {
                attempt_id: quiz.to_dict()
            }
        }
    }

    # WRITE THE DATA TO THE OUTPUT FILE WITH UTF-8 ENCODING
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def load_quiz_attempt(attempt_id: str) -> Quiz:
    """
    LOAD A SPECIFIC QUIZ ATTEMPT FROM A JSON FILE.

    ARGS:
        attempt_id (str): UNIQUE IDENTIFIER OF THE QUIZ ATTEMPT TO LOAD

    RETURNS:
        Quiz: THE LOADED QUIZ OBJECT
    """
    # BUILD THE INPUT FILE PATH
    input_path = os.path.join(QUIZ_ATTEMPT_FOLDER, f"{attempt_id}.json")

    # OPEN AND READ THE JSON FILE
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

        # EXTRACT THE CLASS NAME AS THE TOP-LEVEL KEY
        class_name = next(iter(data))

        # LOAD AND RETURN THE QUIZ OBJECT
        return Quiz.from_dict(data[class_name])

def load_all_quiz_attempts() -> List[Quiz]:
    """
    LOAD ALL SAVED QUIZ ATTEMPTS FROM THE DIRECTORY.

    RETURNS:
        List[Quiz]: A LIST OF ALL LOADED QUIZ OBJECTS
    """
    quizzes = []  # INITIALIZE EMPTY LIST TO STORE QUIZ OBJECTS

    # LOOP THROUGH FILES IN THE QUIZ ATTEMPT FOLDER
    for filename in os.listdir(QUIZ_ATTEMPT_FOLDER):
        if filename.endswith(".json"):
            # OPEN AND READ EACH FILE
            with open(os.path.join(QUIZ_ATTEMPT_FOLDER, filename), "r", encoding="utf-8") as f:
                data = json.load(f)

                # EXTRACT CLASS NAME KEY (ONLY ONE PER FILE)
                class_name = next(iter(data))

                # APPEND THE LOADED QUIZ OBJECT TO THE LIST
                quizzes.append(Quiz.from_dict(data[class_name]))

    return quizzes

def extract_unique_questions_with_correct_answers(quizzes: List[Quiz]):
    """
    EXTRACT UNIQUE QUESTIONS WITH ONLY CORRECT OPTIONS SELECTED.

    ARGS:
        quizzes (List[Quiz]): QUIZ OBJECTS TO PROCESS

    RETURNS:
        List: UNIQUE QUESTIONS WITH ONLY CORRECT OPTIONS RETAINED
    """
    seen = {}  # DICTIONARY TO STORE UNIQUE QUESTIONS BY TEXT

    # LOOP THROUGH ALL QUIZZES AND THEIR QUESTIONS
    for quiz in quizzes:
        for q in quiz.questions:
            # NORMALIZE THE QUESTION TEXT FOR COMPARISON
            key = q.text.strip().lower()

            if key not in seen:
                # FILTER TO ONLY INCLUDE CORRECTLY SELECTED OPTIONS
                correct_opts = [
                    opt for opt in q.options
                    if opt.is_selected and q.points_awarded == q.points_possible
                ]

                # REPLACE OPTIONS WITH ONLY CORRECT ONES, IF FOUND
                if correct_opts:
                    q.options = correct_opts

                # SAVE THE QUESTION UNDER ITS NORMALIZED TEXT
                seen[key] = q

    # RETURN A LIST OF UNIQUE QUESTIONS
    return list(seen.values())
