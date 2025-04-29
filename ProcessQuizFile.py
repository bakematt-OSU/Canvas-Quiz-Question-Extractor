import os
from datetime import datetime
from bs4 import BeautifulSoup


def process_untaken_quiz(file_path, output_file_name, quiz_number, class_name):
    """
    Processes the input HTML file and generates an output text file with quiz results.

    This function reads the content of the provided HTML file, extracts the
    quiz questions and possible answers, and formats the results in a text file with
    details about each question, including the options available.

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

        # Find all questions in the HTML content
        questions = soup.find_all('div', class_='display_question')

        for question_index, question in enumerate(questions, 1):
            # Extract the question text
            question_text_div = question.find('div', class_='question_text')
            question_text = question_text_div.get_text(strip=True) if question_text_div else "No question text found."

            # Write the question to the output file
            output_file.write(f"Question {question_index}:\n")
            output_file.write(f"{question_text}\n")

            # Extract all answer options
            answers = question.find_all('div', class_='answer')
            for idx, answer in enumerate(answers, 1):
                answer_text_div = answer.find('div', class_='answer_label')
                answer_text = answer_text_div.get_text(strip=True) if answer_text_div else "No answer text found."

                # Write the answer options to the file
                output_file.write(f"   Option {idx}: {answer_text}\n")

            output_file.write(f"{'-' * 40}\n")

# Example usage of the modified function:
# process_file("path_to_your_html_file", "output_file.txt", "Quiz3", "CS_370")


# Process the selected file and generate the output file
def process_taken_quiz(file_path, output_file_name, quiz_number, class_name):
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
