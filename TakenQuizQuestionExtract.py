import os
from bs4 import BeautifulSoup
from datetime import datetime

# List all files in the current directory
def list_files():
    files = os.listdir('.')
    print("\nAvailable files in the current directory:")
    for idx, file in enumerate(files, 1):
        print(f"{idx}. {file}")
    return files

# Prompt user to choose input file
def choose_input_file(files):
    while True:
        try:
            file_choice = int(input("\nEnter the number of the file you want to process: ")) - 1
            if file_choice >= 0 and file_choice < len(files):
                return files[file_choice]
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Prompt user to choose output file name
def choose_output_file(quiz_number, class_name):
    current_date = datetime.now().strftime('%Y-%m-%d')
    output_file_name = f"Quiz {quiz_number} - {class_name} - {current_date}.txt"
    return output_file_name

# Prompt user to enter class name, quiz number
def choose_quiz_and_class():
    quiz_number = input("\nEnter the quiz number: ")
    class_name = input("Enter the class name (e.g., 'CS-372 Intro to Networking'): ")
    return quiz_number, class_name

# Load the HTML content from your chosen file
# Process the file and format the output
def process_file(file_path, output_file_name, quiz_number, class_name):
    with open(file_path, 'r') as file:
        html_content = file.read()

    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Open the output file to save the results
    with open(output_file_name, 'w') as output_file:
        current_date = datetime.now().strftime('%Y-%m-%d')
        output_file.write(f"Quiz {quiz_number} - {class_name} - {current_date}\n")
        output_file.write(f"{'-' * 40}\n")

        # Find all questions and answers
        questions = soup.find_all('div', class_='display_question')

        # Extract and write each question with its answers, check correctness, and include unselected answers
        for question_index, question in enumerate(questions, 1):
            
            question_text = question.find('div', class_='question_text').get_text(strip=True)
            question_header = question.find('div',class_='header')
            question_number = question_header.find('span', class_='name question_name').get_text(strip=True)
            # question_wrong = question_header.find('span', class_='answer_arrow incorrect').get_text(strip=True)
            question_wrong = question_header.find('span', class_='answer_arrow incorrect')
            if question_wrong:
                question_wrong_text = question_wrong.get_text(strip=True)
            else:
                question_wrong_text = "Correct"  # or handle it differently as needed
            # Extract points awarded and points possible
            points_awarded = question.find('div', class_='user_points')
            points_possible = question.find('span', class_='points question_points')

            if points_awarded and points_possible:
                points_awarded_text = points_awarded.get_text(strip=True).split()[0]  # Get only the number part (e.g., "6" from "6 / 6 pts")
                points_possible_text = points_possible.get_text(strip=True).split()[1]  # Extract only the number (e.g., "6" from "/ 6 pts")

                # For correct answers
                if question_wrong_text == "Correct":
                    output_file.write(f"----------------------------------------\n")
                    output_file.write(f"{question_number}:\n")
                    output_file.write(f"✔CORRECT - {points_awarded_text}{points_possible_text}pts\n")
                    output_file.write(f"{question_text}\n")
                    
                    answers = question.find_all('div', class_='answer')
                    for idx, answer in enumerate(answers, 1):
                        answer_div = answer.find('div', class_='answer_text')
                        if answer_div:
                            answer_text = answer_div.get_text(strip=True)
                            # is_correct = 'correct' in answer.get('class', [])
                            is_selected = 'selected_answer' in answer.get('class', [])
                            if is_selected:
                                output_file.write(f"   ✔ Option {idx}: {answer_text} - CORRECT\n")
                            else:
                                output_file.write(f"   Option {idx}: {answer_text}\n")

                # For incorrect answers
                else:
                    output_file.write(f"----------------------------------------\n")
                    output_file.write(f"{question_number}:\n")
                    output_file.write(f"❌INCORRECT - {points_awarded_text}{points_possible_text}pts\n")
                    output_file.write(f"{question_text}\n")
                    
                    answers = question.find_all('div', class_='answer')
                    for idx, answer in enumerate(answers, 1):
                        answer_div = answer.find('div', class_='answer_text')
                        if answer_div:
                            answer_text = answer_div.get_text(strip=True)
                            is_correct = 'correct' in answer.get('class', [])
                            is_selected = 'selected_answer' in answer.get('class', [])
                            
                            if is_selected and not is_correct:
                                output_file.write(f"   ❌ Option {idx}: {answer_text} - SELECTED INCORRECT\n")
                            elif is_correct:
                                output_file.write(f"   ✔ Option {idx}: {answer_text} - CORRECT\n")
                            else:
                                output_file.write(f"   Option {idx}: {answer_text}\n")

            else:
                output_file.write(f"----------------------------------------\n")
                output_file.write(f"Question {question_index}:\n")
                output_file.write(f"{question_text}\n")
                output_file.write("Points information not available.\n")

            output_file.write("----------------------------------------\n")

# Main execution
def main():
    files = list_files()  # List files in the current directory
    input_file = choose_input_file(files)  # User selects input file
    quiz_number, class_name = choose_quiz_and_class()  # User enters quiz number and class name
    output_file_name = choose_output_file(quiz_number, class_name)  # Generate output file name

    # Process the selected file and save the results to the output file
    process_file(input_file, output_file_name, quiz_number, class_name)
    print(f"\nResults have been saved to '{output_file_name}'.")

if __name__ == "__main__":
    main()
