import os
from datetime import datetime
from bs4 import BeautifulSoup
import re

def process_untaken_quiz(file_path, output_file_name, quiz_number, class_name):
    """!
    @brief [Description de la fonction]

    Paramètres : 
        @param file_path => [description]
        @param output_file_name => [description]
        @param quiz_number => [description]
        @param class_name => [description]

    """
    """
    Processes the input HTML file and generates an output text file with quiz results.
    Removes NBSP characters from the gathered text.

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
            if question_text_div:
                # question_text = question_text_div.get_text(strip=True)
                question_text = question_text_div.get_text(separator="\n", strip=True)

            else:
                question_text = "No question text found."

            # Remove NBSP characters
            question_text = question_text.replace('\u00A0', ' ')

            # Write the question to the output file
            output_file.write(f"Question {question_index}:\n")
            output_file.write(f"{question_text}\n")

            # Extract all answer options
            answers = question.find_all('div', class_='answer')
            for idx, answer in enumerate(answers, 1):
                answer_text_div = answer.find('div', class_='answer_label')
                answer_text = answer_text_div.get_text(strip=True) if answer_text_div else "No answer text found."

                # Remove NBSP characters
                answer_text = answer_text.replace('\u00A0', ' ')

                # Write the answer options to the file
                output_file.write(f"   Option {idx}: {answer_text}\n")

            output_file.write(f"{'-' * 40}\n")

def process_taken_quiz(file_path, output_file_name, quiz_number, class_name):
    """
    Processes a Canvas quiz HTML file and generates an easy-to-read text document.
    Cleans NBSP characters and handles different types of questions.

    Args:
        file_path (str): Path to the input HTML file.
        output_file_name (str): Path to save the output text file.
        quiz_number (str): Quiz number identifier.
        class_name (str): Class name for labeling output.

    Returns:
        None
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    with open(output_file_name, 'w', encoding='utf-8') as output_file:
        current_date = datetime.now().strftime('%Y-%m-%d')
        output_file.write(f"Quiz {quiz_number} - {class_name} - {current_date}\n")
        output_file.write(f"{'-' * 40}\n")

        questions = soup.find_all('div', class_='display_question')

        for question_index, question in enumerate(questions, 1):
            question_text_div = question.find('div', class_='question_text')
            question_text = question_text_div.get_text(separator=" ", strip=True).replace('\u00A0', ' ') if question_text_div else "No question text found."

            question_header = question.find('div', class_='header')
            question_number = question_header.find('span', class_='name question_name').get_text(strip=True) if question_header else f"Question {question_index}"

            is_correct = question_header.find('span', class_='answer_arrow incorrect') is None

            points_awarded_elem = question.find('div', class_='user_points')
            points_possible_elem = question.find('span', class_='points question_points')

            if points_awarded_elem and points_possible_elem:
                points_awarded_text = points_awarded_elem.get_text(strip=True).split()[0]
                points_possible_parts = points_possible_elem.get_text(strip=True).split()

                try:
                    points_awarded = float(re.search(r'[\d.]+', points_awarded_text).group())
                    points_possible = float(points_possible_parts[-1])  # Safely grab the last number
                except (AttributeError, IndexError, ValueError):
                    points_awarded = points_possible = 0.0

                output_file.write(f"{'-' * 40}\n")
                output_file.write(f"{question_number}:\n")
                output_file.write(f"{'✔ CORRECT' if is_correct else '❌ INCORRECT'} - {points_awarded}/{points_possible}pts\n")
                output_file.write(f"{question_text}\n")

                # Handle numerical input answers (standard)
                given_answer_div = question.find('div', class_='form-control numerical-question-holder')
                # Handle text-box input answers (short answer)
                answer_text_boxes = question.find_all('div', class_='form-control text-box-question-holder')
                # Handle MC/Matching
                answers = question.find_all('div', class_='answer')

                if given_answer_div:
                    # Standard numerical input
                    given_answer_input = given_answer_div.find('input', type='text')
                    given_answer_text = given_answer_input.get('value', '').strip() if given_answer_input else "NO ANSWER GIVEN"
                    output_file.write(f"   {'✔ - CORRECT:' if is_correct else '❌ - INCORRECT:'} Given Answer: {given_answer_text}\n")

                elif answer_text_boxes:
                    # Short-answer text box inputs (can be multiple)
                    for idx, text_box in enumerate(answer_text_boxes, 1):
                        input_tag = text_box.find('input', type='text')
                        value = input_tag.get('value', '').strip() if input_tag else "NO ANSWER GIVEN"
                        output_file.write(f"   {'✔ - CORRECT:' if is_correct else '❌ - INCORRECT:'} Text {idx}: {value}\n")

                else:
                    # Handle multiple choice or matching
                    for idx, answer in enumerate(answers, 1):
                        match_left = answer.find('div', class_='answer_match_left')
                        match_right = answer.find('select')
                        correct_span = answer.find('span', class_='answer_arrow correct')
                        is_selected = 'selected_answer' in answer.get('class', [])

                        if match_left and match_right:
                            prompt = match_left.get_text(strip=True).replace('\u00A0', ' ')
                            selected_option = match_right.find('option', selected=True)
                            selected_text = selected_option.get_text(strip=True) if selected_option else "Not selected"
                            output_file.write(f"   {'✔ - CORRECT:' if is_correct else '❌ - INCORRECT:'} Option {idx}: {prompt} {selected_text}\n")
                        else:
                            answer_text_div = answer.find('div', class_='answer_text')
                            if answer_text_div:
                                answer_text = answer_text_div.get_text(strip=True).replace('\u00A0', ' ')
                                if is_selected:
                                    output_file.write(f"   {'✔ - CORRECT:' if is_correct else '❌ - INCORRECT:'} Option {idx}: {answer_text} (Selected)\n")
                                else:
                                    output_file.write(f"   Option {idx}: {answer_text}\n")

            else:
                output_file.write(f"{'-' * 40}\n")
                output_file.write(f"{question_number}:\n")
                output_file.write(f"{question_text}\n")
                output_file.write("Points information not available.\n")

            output_file.write(f"{'-' * 40}\n")
