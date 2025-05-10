"""
CANVAS QUIZ ARCHIVER

THIS SCRIPT PROMPTS THE USER FOR CLASS AND QUIZ METADATA, PARSES A QUIZ HTML FILE,
AND ARCHIVES THE QUIZ TO A JSON FILE WITH A UNIQUE ATTEMPT ID.

FUNCTIONS:
- LIST_HTML_FILES: RETURNS A LIST OF HTML FILES IN A DIRECTORY.
- CHOOSE_INPUT_FILE: PROMPTS THE USER TO SELECT A FILE.
- READ_CLASSES_FROM_FILE: LOADS AVAILABLE CLASSES FROM A FILE.
- CHOOSE_QUIZ_AND_CLASS: PROMPTS THE USER FOR CLASS AND QUIZ INFORMATION.
- MAIN: EXECUTES THE EXTRACTION AND ARCHIVAL WORKFLOW.
"""

import os
from datetime import datetime
from quiz_extractor import parse_quiz_html
from quiz_core_utils import save_quiz_attempt

def list_html_files(directory):
    """
    LIST ALL HTML FILES IN A DIRECTORY.

    ARGS:
        directory (str): PATH TO LOOK FOR FILES

    RETURNS:
        list: HTML FILE NAMES
    """
    # RETURN LIST OF FILES THAT END IN .HTML
    return [f for f in os.listdir(directory) if f.endswith('.html')]

def choose_input_file(files):
    """
    PROMPT USER TO SELECT A FILE.

    ARGS:
        files (list): AVAILABLE FILE OPTIONS

    RETURNS:
        str: SELECTED FILE NAME
    """
    # DISPLAY FILE OPTIONS
    print("\nAVAILABLE HTML FILES:")
    for idx, f in enumerate(files, 1):
        print(f"{idx}. {f}")
    # PROMPT USER FOR CHOICE
    choice = int(input("\nCHOOSE A FILE BY NUMBER: ")) - 1
    return files[choice]

def read_classes_from_file(filename):
    """
    READ CLASS OPTIONS FROM FILE.

    ARGS:
        filename (str): FILE CONTAINING CLASS NAMES

    RETURNS:
        list: CLASS NAMES
    """
    try:
        # READ AND STRIP NON-BLANK LINES FROM FILE
        with open(filename, 'r') as file:
            classes = [line.strip() for line in file.readlines() if line.strip()]
        return classes
    except FileNotFoundError:
        # DISPLAY ERROR IF FILE NOT FOUND
        print(f"THE FILE {filename} WAS NOT FOUND.")
        return []

def choose_quiz_and_class():
    """
    PROMPT USER TO SELECT CLASS AND INPUT QUIZ NUMBER.

    RETURNS:
        tuple: (QUIZ_NUMBER, CLASS_NAME)
    """
    # READ CLASSES FROM FILE
    classes = read_classes_from_file("CurrentClasses.txt")
    print("AVAILABLE OPTIONS:")
    print("0. ENTER CLASS INFO MANUALLY")

    # DISPLAY AVAILABLE CLASS OPTIONS
    if classes:
        for idx, class_info in enumerate(classes, 1):
            print(f"{idx}. {class_info}")

    # GET CLASS SELECTION
    choice = int(input("\nSELECT A CLASS BY NUMBER: "))

    if choice == 0:
        # USER ENTERS CLASS INFO MANUALLY
        class_name = input("ENTER THE CLASS NAME MANUALLY: ")
        quiz_number = input("ENTER THE QUIZ NUMBER: ")
    elif 1 <= choice <= len(classes):
        # USER SELECTS EXISTING CLASS
        class_name = classes[choice - 1]
        quiz_number = input(f"ENTER THE QUIZ NUMBER FOR {class_name}: ")
    else:
        # INVALID SELECTION — RECURSIVELY PROMPT AGAIN
        print("INVALID SELECTION. TRY AGAIN.")
        return choose_quiz_and_class()

    # OPTIONALLY APPEND EXTRA INFO TO QUIZ NUMBER
    while True:
        extra_info_input = input("IS THERE ANY EXTRA INFO FOR THIS QUIZ? (1=YES, 0=NO): ").strip()
        if extra_info_input == '1':
            extra_info = input("ENTER EXTRA INFO: ")
            quiz_number += ' - ' + extra_info
            break
        elif extra_info_input == '0':
            break
        else:
            print("INVALID INPUT. ENTER 1 OR 0.")

    return quiz_number, class_name

def main():
    """
    MAIN FUNCTION TO EXTRACT AND SAVE QUIZ ATTEMPT.
    """
    # SET INPUT DIRECTORY
    input_dir = "Input"
    
    # LIST HTML FILES IN INPUT DIRECTORY
    html_files = list_html_files(input_dir)

    # PROMPT FOR STUDENT NAME
    student_name = input("ENTER STUDENT NAME: ").strip()

    # HANDLE NO FILES CASE
    if not html_files:
        print("NO HTML FILES FOUND.")
        return

    # PROMPT USER TO SELECT A FILE
    file_name = choose_input_file(html_files)
    file_path = os.path.join(input_dir, file_name)

    # PROMPT FOR CLASS AND QUIZ DETAILS
    quiz_title, class_name = choose_quiz_and_class()

    # PROMPT FOR UNIQUE ATTEMPT ID
    attempt_id = input("ENTER A UNIQUE ATTEMPT ID (e.g. '1'): ").strip()

    # PARSE QUIZ HTML INTO A QUIZ OBJECT
    quiz = parse_quiz_html(file_path, quiz_title)

    # SAVE QUIZ ATTEMPT TO JSON ARCHIVE
    # save_quiz_attempt(quiz, attempt_id, class_name)
    save_quiz_attempt(quiz, attempt_id, class_name, student_name)

    # CONFIRM SUCCESS
    print(f"\n✅ QUIZ '{quiz_title}' SAVED SUCCESSFULLY UNDER ID '{attempt_id}'.")

# RUN MAIN FUNCTION IF THIS FILE IS EXECUTED DIRECTLY
if __name__ == "__main__":
    main()
