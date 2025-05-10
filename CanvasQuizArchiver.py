"""
Canvas:   Quiz Extractor
Author:   Matthew Baker
Brief:    Prompts user for quiz context and saves parsed quiz attempt to structured archive.
Version:  1.0
Date:     2025-05-09
"""

import os
from datetime import datetime
from quiz_extractor import parse_quiz_html
from quiz_core_utils import save_quiz_attempt

def list_html_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.html')]

def choose_input_file(files):
    print("\nAvailable HTML files:")
    for idx, f in enumerate(files, 1):
        print(f"{idx}. {f}")
    choice = int(input("\nChoose a file by number: ")) - 1
    return files[choice]

def prompt_for_metadata():
    quiz_title = input("Enter the title of the quiz: ").strip()
    attempt_id = input("Enter a unique attempt ID (e.g. 'CS370-Quiz6-v1'): ").strip()
    return quiz_title, attempt_id

def main():
    input_dir = "Input"
    html_files = list_html_files(input_dir)

    if not html_files:
        print("No HTML files found in the Input folder.")
        return

    file_name = choose_input_file(html_files)
    file_path = os.path.join(input_dir, file_name)
    quiz_title, attempt_id = prompt_for_metadata()

    quiz = parse_quiz_html(file_path, quiz_title)
    save_quiz_attempt(quiz, attempt_id)

    print(f"\n✅ Quiz '{quiz_title}' saved successfully under ID '{attempt_id}'.")

if __name__ == "__main__":
    main()
