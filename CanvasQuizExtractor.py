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
import ProcessQuizFile

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

# Prompt user to select quiz extraction method
def choose_extraction_method():
    """
    Prompts the user to choose between "Quiz Question Only Extraction" and "Taken Quiz Extraction & Answer" quiz extraction method.

    This function presents the user with the options and returns the chosen method.

    Returns:
        str: The selected extraction method (1 or 2).
    """
    while True:
        print("\nSelect the quiz extraction method:")
        print("1. Taken Quiz Extraction ➡ Returns: Questions, Answers, and marks Question Correct or Incorrect")
        print("2. Untaken Quiz Extraction ➡ Returns: Questions, and Possible Options")
        try:
            choice = int(input("\nEnter the number of your choice: "))
            if choice == 1:
                return 1
            elif choice == 2:
                return 2
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main function to process the file
def main():
    """
    Main function to drive the process of selecting a file and generating the output file.

    This function orchestrates the workflow: listing available files, allowing the user to
    choose an input file, entering quiz number and class name, selecting the extraction method,
    and processing the selected file to generate the output file with the quiz results.

    Returns:
        None
    """
    extraction_method = choose_extraction_method()  # Choose quiz extraction method
    files = list_files()  # List files in the current directory
    input_file = choose_input_file(files)  # User selects input file
    quiz_number, class_name = choose_quiz_and_class()  # User enters quiz number and class name
    output_file_name = choose_output_file(quiz_number, class_name)  # Generate output file name
    

    if extraction_method == 1:
        # Process the selected file and save the results to the output file
        ProcessQuizFile.process_taken_quiz(input_file, output_file_name, quiz_number, class_name)
        print(f"\nResults have been saved to '{output_file_name}'.")
    elif extraction_method == 2:
        # Process the selected file and save the results to the output file
        ProcessQuizFile.process_untaken_quiz(input_file, output_file_name, quiz_number, class_name)
        print(f"\nResults have been saved to '{output_file_name}'.")
    else:
        print("ERROR - No matching Extraction Method")

if __name__ == "__main__":
    main()
