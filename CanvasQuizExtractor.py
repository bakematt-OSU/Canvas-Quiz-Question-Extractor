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
import HTML_Extract
import FileProcess


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

def choose_quiz_and_class():
    """
    Prompts the user to select a class and enter the quiz number, and asks for
    any additional information related to the quiz.

    This function displays available classes and allows the user to either
    select a class from the list or enter the class name manually. It also
    prompts the user for the quiz number and any extra information.

    Returns:
        tuple: A tuple containing the quiz number (str), the class name (str), 
               and the extra information (str, optional).
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

    # Ask if there is any extra information after the quiz number
    while True:
        extra_info_input = input("Is there any extra information for this quiz? (1 for yes, 0 for no): ").strip()

        if extra_info_input == '1':
            extra_info = input("Please enter the extra information: ")
            break
        elif extra_info_input == '0':
            extra_info = ""
            break
        else:
            print("Invalid input. Please enter '1' for yes or '0' for no.")
    quiz_number = quiz_number + ' - '+extra_info
    
    return quiz_number, class_name


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
    files = FileProcess.list_files()  # List files in the current directory
    if files:
        input_file = FileProcess.choose_input_file(files)  # User selects input file
        quiz_number, class_name = choose_quiz_and_class()  # User enters quiz number and class name
        output_file_name = FileProcess.choose_output_file(quiz_number, class_name)  # Generate output file name
        if extraction_method == 1:
            # Process the selected file and save the results to the output file
            HTML_Extract.process_taken_quiz(input_file, output_file_name, quiz_number, class_name)
            print(f"\nResults have been saved to '{output_file_name}'.")
        elif extraction_method == 2:
            # Process the selected file and save the results to the output file
            HTML_Extract.process_untaken_quiz(input_file, output_file_name, quiz_number, class_name)
            print(f"\nResults have been saved to '{output_file_name}'.")
        else:
            print("ERROR - No matching Extraction Method")


if __name__ == "__main__":
    main()
