'''
Canvas:   Quiz Extractor
Author:   Matthew Baker
Brief:    Takes HTML file of Quiz results from Canvas and creates a Easy to read Text Document for Studying or Flash Card Making.
Version:  0.1
Date:     2025-04-12
'''

import os
from datetime import datetime
from bs4 import BeautifulSoup

# List all files in the current directory
def list_files():
    """
    Lists all files in the current directory.

    This function prints all the files available in the current working
    directory and returns them as a list of file names.

    Returns:
        list: A list of filenames in the current directory.
    """
    files = os.listdir('.')
    print("\nAvailable files in the current directory:")
    for idx, file in enumerate(files, 1):
        print(f"{idx}. {file}")
    return files

# Function to read class info from CurrentClasses.txt
def read_classes_from_file(filename):
    """
    Reads class information from a specified file.

    This function attempts to read class names from a file where each class
    is listed on a separate line. It returns the list of class names, or
    an empty list if the file is not found.

    Args:
        filename (str): The path to the file containing class information.

    Returns:
        list: A list of class names read from the file. If the file is not
              found, an empty list is returned.
    """
    try:
        with open(filename, 'r') as file:
            classes = [line.strip() for line in file.readlines() if line.strip()]
        return classes
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return []

# Prompt user to choose input file
def choose_input_file(files):
    """
    Prompts the user to choose an input file from a list of available files.

    This function displays a list of files and allows the user to select
    a file by entering its corresponding number.

    Args:
        files (list): A list of file names available for selection.

    Returns:
        str: The name of the selected file.
    """
    while True:
        try:
            file_choice = int(input("\nEnter the number of the file you want to process: ")) - 1
            if file_choice >= 0 and file_choice < len(files):
                return files[file_choice]
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Prompt user to choose quiz number and class name
def choose_quiz_and_class():
    """
    Prompts the user to select a class and enter the quiz number.

    This function displays available classes and allows the user to either
    select a class from the list or enter the class name manually. It also
    prompts the user for the quiz number.

    Returns:
        tuple: A tuple containing the quiz number (str) and the class name (str).
    """
    classes = read_classes_from_file("CurrentClasses.txt")
    print("Available options:")
    
    # Option 0 is for entering manually
    print("0. Enter class info manually")

    if classes:
        for idx, class_info in enumerate(classes, 1):
            print(f"{idx}. {class_info}")

    choice = int(input("\nSelect a class by number: "))

    if choice == 0:
        class_name = input("Enter the class name manually: ")
        quiz_number = input("Enter the quiz number: ")
    elif 1 <= choice <= len(classes):
        class_name = classes[choice - 1]
        quiz_number = input(f"Enter the quiz number for {class_name}: ")
    else:
        print("Invalid selection. Please try again.")
        return choose_quiz_and_class()

    return quiz_number, class_name

# Prompt user to choose output file name
def choose_output_file(quiz_number, class_name):
    """
    Generates the output file name based on quiz number, class name, and current date.

    This function constructs a file name that follows the format:
    'Quiz <quiz_number> - <class_name> - <current_date>.txt'

    Args:
        quiz_number (str): The quiz number.
        class_name (str): The name of the class.

    Returns:
        str: The generated output file name.
    """
    current_date = datetime.now().strftime('%Y-%m-%d')
    output_file_name = f"Quiz {quiz_number} - {class_name} - {current_date}.txt"
    return output_file_name

# Process the selected file and generate the output file
def process_file(file_path, output_file_name, quiz_number, class_name):
    """
    Processes the input HTML file and generates an output text file with quiz results.

    This function reads the content of the provided HTML file, extracts the
    quiz questions and answers, and formats the results in a text file with
    details about each question, including whether the answer was correct,
    the points awarded, and the options selected.

    Args:
        file_path (str): The path to the input HTML file.
        output_file_name (str): The path to the output file where results will be saved.
        quiz_number (str): The quiz number.
        class_name (str): The class name.

    Returns:
        None
    """
    with open(file_path, 'r') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Open the output file to save the results
    with open(output_file_name, 'w') as output_file:
        current_date = datetime.now().strftime('%Y-%m-%d')
        output_file.write(f"Quiz {quiz_number} - {class_name} - {current_date}\n")
        output_file.write(f"{'-' * 40}\n")

        # Find all questions and answers
        questions = soup.find_all('div', class_='display_question')

        for question_index, question in enumerate(questions, 1):
            # Extract question text
            question_text = question.find('div', class_='question_text')
            if question_text:
                question_text = question_text.get_text(strip=True)
            else:
                question_text = "No question text found."

            # Extract question number
            question_header = question.find('div', class_='header')
            question_number = question_header.find('span', class_='name question_name').get_text(strip=True)

            # Check if the answer is correct or incorrect
            question_wrong = question_header.find('span', class_='answer_arrow incorrect')
            if question_wrong:
                question_wrong_text = "INCORRECT"
            else:
                question_wrong_text = "CORRECT"

            # Extract points awarded and points possible
            points_awarded = question.find('div', class_='user_points')
            points_possible = question.find('span', class_='points question_points')

            if points_awarded and points_possible:
                points_awarded_text = points_awarded.get_text(strip=True).split()[0]  # Extract points awarded
                points_possible_text = points_possible.get_text(strip=True).split()[1]  # Extract total points

                # For correct answers
                if question_wrong_text == "CORRECT":
                    output_file.write(f"----------------------------------------\n")
                    output_file.write(f"{question_number}:\n")
                    output_file.write(f"✔CORRECT - {points_awarded_text}{points_possible_text}pts\n")
                    output_file.write(f"{question_text}\n")
                else:
                    output_file.write(f"----------------------------------------\n")
                    output_file.write(f"{question_number}:\n")
                    output_file.write(f"❌INCORRECT - {points_awarded_text}{points_possible_text}pts\n")
                    output_file.write(f"{question_text}\n")

                # Try to extract the given answer (from input element inside the div with 'form-control numerical-question-holder')
                given_answer_div = question.find('div', class_='form-control numerical-question-holder')
                if given_answer_div:
                    given_answer_input = given_answer_div.find('input', type='text')
                    if given_answer_input:
                        given_answer_text = given_answer_input.get('value', 'Answer not available')
                    else:
                        given_answer_text = "NO ANSWER GIVEN"
                    # Write the given answer to the file
                    if question_wrong_text == "CORRECT":
                        output_file.write(f"   ✔Given Answer: {given_answer_text} - CORRECT\n")
                    else:
                        output_file.write(f"   ❌Given Answer: {given_answer_text} - INCORRECT\n")

                else:
                    # Extract and write the answers for non fill in the blank
                    answers = question.find_all('div', class_='answer')
                    for idx, answer in enumerate(answers, 1):
                        answer_div = answer.find('div', class_='answer_text')
                        if answer_div:
                            answer_text = answer_div.get_text(strip=True)
                            is_selected = 'selected_answer' in answer.get('class', [])
                            is_correct = 'correct' in answer.get('class', [])

                            # Check if the answer was selected and whether it's correct or not
                            if is_selected:
                                if question_wrong_text == "CORRECT":
                                    output_file.write(f"   ✔ Option {idx}: {answer_text} - CORRECT\n")
                                else:
                                    output_file.write(f"   ❌ Option {idx}: {answer_text} - SELECTED INCORRECT\n")
                            else:
                                    output_file.write(f"   Option {idx}: {answer_text}\n")

            else:
                output_file.write(f"----------------------------------------\n")
                output_file.write(f"Question {question_index}:\n")
                output_file.write(f"{question_text}\n")
                output_file.write("Points information not available.\n")

            output_file.write("----------------------------------------\n")

# Main function to process the file
def main():
    """
    Main function to drive the process of selecting a file and generating the output file.

    This function orchestrates the workflow: listing available files, allowing the user to
    choose an input file, entering quiz number and class name, and processing the selected
    file to generate the output file with the quiz results.

    Returns:
        None
    """
    files = list_files()  # List files in the current directory
    input_file = choose_input_file(files)  # User selects input file
    quiz_number, class_name = choose_quiz_and_class()  # User enters quiz number and class name
    output_file_name = choose_output_file(quiz_number, class_name)  # Generate output file name

    # Process the selected file and save the results to the output file
    process_file(input_file, output_file_name, quiz_number, class_name)
    print(f"\nResults have been saved to '{output_file_name}'.")

if __name__ == "__main__":
    main()
