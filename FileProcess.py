import os
from datetime import datetime

# Define global variables for the input and output directories
INPUT_FOLDER = "Input"
OUTPUT_FOLDER = "Output"

def list_files():
    """
    Lists all files in the 'Input' directory.

    This function prints all the files available in the 'Input' directory
    and returns them as a list of file names.

    Returns:
        list: A list of filenames in the 'Input' directory.
    """
    
    # Check if the Input directory exists
    if not os.path.exists(INPUT_FOLDER):
        print(f"The directory {INPUT_FOLDER} does not exist.")
        return []
    
    # Get the list of files in the Input directory
    files = [f for f in os.listdir(INPUT_FOLDER) if os.path.isfile(os.path.join(INPUT_FOLDER, f))]
    
    if not files:
        print(f"There are no files in the {INPUT_FOLDER} directory.")
        return []
    
    # Display the list of available files
    print(f"\nAvailable files in the '{INPUT_FOLDER}' directory:")
    for idx, file in enumerate(files, 1):
        print(f"{idx}. {file}")
    
    return files


def choose_input_file(files):
    """
    Prompts the user to choose an input file from a list of available files in the 'InputFiles' folder.

    This function lists all files in the 'InputFiles' directory and allows the user to select
    a file by entering its corresponding number.

    Returns:
        str: The name of the selected file.
    """
    
    
    # Display the list of available files
    print("\nAvailable files in the 'InputFiles' directory:")
    for idx, file in enumerate(files, 1):
        print(f"{idx}. {file}")
    
    # Prompt the user to select a file
    while True:
        try:
            file_choice = int(input("\nEnter the number of the file you want to process: ")) - 1
            if file_choice >= 0 and file_choice < len(files):
                return os.path.join(INPUT_FOLDER, files[file_choice])
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def choose_output_file(quiz_number, class_name):
    """
    Generates the output file name based on quiz number, class name, and current date,
    saves it in the 'Output' folder, and prompts the user whether to overwrite or 
    rename the file with attempts if a file with the same name already exists.

    Args:
        quiz_number (str): The quiz number.
        class_name (str): The name of the class.

    Returns:
        str: The full path of the generated output file name.
    """
    
    # Check if the Output directory exists, if not, create it
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    
    # Get the current date in 'YYYY-MM-DD' format
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Construct the base output file name
    output_file_name = f"Quiz {quiz_number} - {class_name} - {current_date}.txt"
    
    # Full path to check if the file already exists
    output_file_path = os.path.join(OUTPUT_FOLDER, output_file_name)
    
    # Check if the file already exists
    if os.path.exists(output_file_path):
        # Prompt the user for an action if file exists
        while True:
            user_choice = input(f"The file '{output_file_name}' already exists. Do you want to overwrite it? (y/n) or rename it with attempts (a): ").lower()
            
            if user_choice == 'y':  # Overwrite the file
                print("Overwriting the existing file.")
                break
            elif user_choice == 'n':  # Don't overwrite and return the existing name
                print("File will not be overwritten. Please choose a different file name.")
                return None  # No file is returned since no overwrite is allowed
            elif user_choice == 'a':  # Rename with attempt number
                attempt_number = 1
                base_name, ext = os.path.splitext(output_file_name)
                
                # Generate a new file name with attempt number
                while os.path.exists(output_file_path):
                    output_file_name = f"{base_name} - Attempt {attempt_number}{ext}"
                    output_file_path = os.path.join(OUTPUT_FOLDER, output_file_name)
                    attempt_number += 1
                
                print(f"File renamed to '{output_file_name}' and will be saved.")
                break
            else:
                print("Invalid input. Please choose 'y' to overwrite, 'n' to not overwrite, or 'a' to rename with attempts.")
    
    # Return the full path for the file
    return output_file_path




def OLD_choose_output_file(quiz_number, class_name):
    """
    Generates the output file name based on quiz number, class name, and current date, and saves it in the 'Output' folder.

    This function constructs a file name that follows the format:
    'Quiz <quiz_number> - <class_name> - <current_date>.txt'
    and ensures the file is saved in the 'Output' directory.

    Args:
        quiz_number (str): The quiz number.
        class_name (str): The name of the class.

    Returns:
        str: The full path of the generated output file name.
    """
    
    # Check if the Output directory exists, if not, create it
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    
    # Get the current date in 'YYYY-MM-DD' format
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Construct the output file name
    output_file_name = f"Quiz {quiz_number} - {class_name} - {current_date}.txt"
    
    # Return the full path for the file in the Output folder
    return os.path.join(OUTPUT_FOLDER, output_file_name)


# List all files in the current directory
def OLD_list_files():
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


# Prompt user to choose output file name
def OLD_choose_output_file(quiz_number, class_name):
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



# Prompt user to choose input file
def OLD_choose_input_file(files):
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
