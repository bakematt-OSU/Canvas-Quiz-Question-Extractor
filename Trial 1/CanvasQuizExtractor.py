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
    output_file_name = f"Quiz {quiz_number} - {quiz_number} - {current_date}.txt"
    return output_file_name

# Prompt user to enter class name, quiz number
def choose_quiz_and_class():
    quiz_number = input("\nEnter the quiz number: ")
    class_name = input("Enter the class name (e.g., 'CS-372 Intro to Networking'): ")
    return quiz_number, class_name

# Load the HTML content from your chosen file
def process_file(file_path, output_file_name, quiz_number, class_name):
    with open(file_path, 'r') as file:
        html_content = file.read()

    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Open the output file to save the results
    with open(output_file_name, 'w') as output_file:
        current_date = datetime.now().strftime('%Y-%m-%d')
        output_file.write(f"Quiz {quiz_number} - {quiz_number} - {current_date}\n")
        output_file.write(f"{'-' * 40}\n")
        output_file.write(f"{'-' * 40}\n")  # Blank line between quiz info and first question

        # Find all questions and answers
        questions = soup.find_all('div', class_='display_question')

        # Extract and write each question with its answers, points, correctness, and include unselected answers
        for question_index, question in enumerate(questions, 1):
            question_text = question.find('div', class_='question_text').get_text(strip=True)
            
            # Find points earned and possible points
            points_earned = question.find('span', class_='user_points')
            possible_points = question.find('span', class_='question_points')

            # Extract points earned and possible points
            earned = points_earned.get_text(strip=True) if points_earned else "N/A"
            possible = possible_points.get_text(strip=True) if possible_points else "N/A"

            # Write the question and points
            output_file.write(f"Question {question_index} - {earned} / {possible}:\n")
            output_file.write(f"{question_text}\n")
            output_file.write(f"{'-' * 40}\n")

            # Track whether there are selected answers and unselected answers
            selected_answers = []
            unselected_answers = []

            answers = question.find_all('div', class_='answer')
            for idx, answer in enumerate(answers, 1):
                answer_div = answer.find('div', class_='answer_text')
                if answer_div:
                    answer_text = answer_div.get_text(strip=True)
                    is_correct = 'correct' in answer.get('class', [])
                    is_selected = 'selected_answer' in answer.get('class', [])

                    # Collect selected and unselected answers
                    if is_selected:
                        selected_answers.append(f"  ✔ Option {idx}: {answer_text} - Correct")
                    else:
                        unselected_answers.append(f"  ❌ Option {idx}: {answer_text} - Incorrect")
                else:
                    print(f"Answer {idx} does not have an 'answer_text' class.")

            # Write selected answers first
            for selected in selected_answers:
                output_file.write(f"{selected}\n")

            # Then write unselected answers
            for unselected in unselected_answers:
                output_file.write(f"{unselected}\n")

            output_file.write(f"{'-' * 40}\n")
            output_file.write(f"{'-' * 40}\n")  # Blank line after each question

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
