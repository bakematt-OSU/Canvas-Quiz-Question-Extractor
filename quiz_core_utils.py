"""
QUIZ CORE UTILITIES MODULE

THIS MODULE HANDLES THE SAVING, LOADING, AND PROCESSING OF QUIZ ATTEMPT DATA.
IT SAVES QUIZZES IN THE FORMAT: CLASS -> QUIZ -> ATTEMPT -> QUIZ_DATA
"""

import os
import json
from typing import List
from quiz_models import Quiz

# DEFINE THE FOLDER WHERE QUIZ ATTEMPT FILES WILL BE STORED
QUIZ_ATTEMPT_FOLDER = "_data"
QUIZ_DATA = "quiz_data.json"

# CREATE THE FOLDER IF IT DOES NOT ALREADY EXIST
os.makedirs(QUIZ_ATTEMPT_FOLDER, exist_ok=True)


def save_quiz_attempt(quiz: Quiz, attempt_id: str, class_name: str):
    """
    SAVE A QUIZ ATTEMPT TO A JSON FILE USING THE STRUCTURE:
    CLASS -> QUIZ -> ATTEMPT -> QUIZ DATA

    ARGS:
        quiz (Quiz): THE QUIZ ATTEMPT TO BE SAVED
        attempt_id (str): UNIQUE IDENTIFIER FOR THE ATTEMPT
        class_name (str): NAME OF THE CLASS FOR ORGANIZATION

    RETURNS:
        NONE
    """
    # CREATE A DIRECTORY FOR THE CLASS IF NOT EXISTS
    # class_folder = os.path.join(QUIZ_ATTEMPT_FOLDER, class_name)
    # os.makedirs(class_folder, exist_ok=True)

    # FILE PATH FORMAT: quiz_attempts/CLASS/QUIZ.json
    quiz_file = os.path.join(QUIZ_ATTEMPT_FOLDER, QUIZ_DATA)

    # LOAD EXISTING DATA IF FILE EXISTS
    if os.path.exists(quiz_file):
        with open(quiz_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {}

    # INSERT QUIZ DATA UNDER STRUCTURE: CLASS -> QUIZ -> ATTEMPT
    if class_name not in data:
        data[class_name] = {}
    if quiz.title not in data[class_name]:
        data[class_name][quiz.title] = {}

    data[class_name][quiz.title][attempt_id] = quiz.to_dict()

    # WRITE BACK TO FILE
    with open(quiz_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_quiz_attempt(class_name: str, quiz_title: str, attempt_id: str) -> Quiz:
    """
    LOAD A SPECIFIC QUIZ ATTEMPT BASED ON CLASS, QUIZ, AND ATTEMPT ID.

    ARGS:
        class_name (str): THE NAME OF THE CLASS
        quiz_title (str): THE TITLE OF THE QUIZ
        attempt_id (str): THE ATTEMPT ID TO LOAD

    RETURNS:
        Quiz: THE LOADED QUIZ OBJECT
    """
    file_path = os.path.join(QUIZ_ATTEMPT_FOLDER, QUIZ_DATA)

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    quiz_data = data[class_name][quiz_title][attempt_id]
    return Quiz.from_dict(quiz_data)


def load_all_quiz_attempts() -> List[Quiz]:
    """
    LOAD ALL QUIZ ATTEMPTS FROM THE FLAT quiz_data.json FILE STRUCTURE.

    RETURNS:
        List[Quiz]: A LIST OF ALL QUIZ ATTEMPTS
    """
    quizzes = []
    file_path = os.path.join(QUIZ_ATTEMPT_FOLDER, QUIZ_DATA)

    if not os.path.exists(file_path):
        return quizzes  # RETURN EMPTY LIST IF FILE DOESN'T EXIST

    # LOAD THE JSON FILE
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # ITERATE THROUGH CLASS -> QUIZ -> ATTEMPT STRUCTURE
    for class_name, quizzes_by_title in data.items():
        for quiz_title, attempts in quizzes_by_title.items():
            for attempt_id, quiz_data in attempts.items():
                quizzes.append(Quiz.from_dict(quiz_data))

    return quizzes
