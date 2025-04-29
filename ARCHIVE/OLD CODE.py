
def Before_process_taken_quiz(file_path, output_file_name, quiz_number, class_name):
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

        # Find all questions and answers
        questions = soup.find_all('div', class_='display_question')

        for question_index, question in enumerate(questions, 1):
            # Extract question text
            question_text = question.find('div', class_='question_text')
            if question_text:
                question_text = question_text.get_text(strip=True)
            else:
                question_text = "No question text found."

            # Remove NBSP characters
            question_text = question_text.replace('\u00A0', ' ')

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

                            # Remove NBSP characters from answer text
                            answer_text = answer_text.replace('\u00A0', ' ')

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



def OLD_process_taken_quiz(file_path, output_file_name, quiz_number, class_name):
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

    soup = BeautifulSoup(html_content, 'html.parser')

    with open(output_file_name, 'w') as output_file:
        current_date = datetime.now().strftime('%Y-%m-%d')
        output_file.write(f"Quiz {quiz_number} - {class_name} - {current_date}\n")
        output_file.write(f"{'-' * 40}\n")
        question_container = soup.find_all('div', class_='assessment_results')

        questions = soup.find_all('div', class_='display_question')

        for question_index, question in enumerate(questions, 1):
            question_text_div = question.find('div', class_='question_text')
            # Extract the question text
            question_text_div = question.find('div', class_='question_text')
            if question_text_div:
                # question_text = question_text_div.get_text(strip=True)
                question_text = question_text_div.get_text(separator=" ", strip=True)

            else:
                question_text = "No question text found."
                
            question_text = question_text.replace('\u00A0', ' ')

            question_header = question.find('div', class_='header')
            question_number = question_header.find('span', class_='name question_name').get_text(strip=True)

            question_wrong = question_header.find('span', class_='answer_arrow incorrect')
            if question_wrong:
                question_wrong_text = "INCORRECT"
            else:
                question_wrong_text = "CORRECT"

            points_awarded = question.find('div', class_='user_points')
            points_possible = question.find('span', class_='points question_points')

            if points_awarded and points_possible:
                points_awarded_text = points_awarded.get_text(strip=True).split()[0]
                points_possible_text = points_possible.get_text(strip=True).split()[1]
                
                points_awarded_match = re.search(r'[\d.]+', points_awarded_text)
                if points_awarded_match:
                    points_awarded_numeric = float(points_awarded_match.group())
                    points_possible_numeric = float(points_possible_text)
                   
                

                output_file.write(f"{'-' * 40}\n")
                output_file.write(f"{question_number}:\n")
                if question_wrong_text == "CORRECT":
                    output_file.write(f"\u2714CORRECT - {points_awarded_numeric}/{points_possible_numeric}pts\n")
                else:
                    output_file.write(f"\u274CINCORRECT - {points_awarded_numeric}/{points_possible_numeric}pts\n")
                output_file.write(f"{question_text}\n")

                given_answer_div = question.find('div', class_='form-control numerical-question-holder')
                if given_answer_div:
                    given_answer_input = given_answer_div.find('input', type='text')
                    if given_answer_input:
                        given_answer_text = given_answer_input.get('value', 'Answer not available')
                    else:
                        given_answer_text = "NO ANSWER GIVEN"
                    if question_wrong_text == "CORRECT":
                        output_file.write(f"   \u2714Given Answer: {given_answer_text} - CORRECT\n")
                    else:
                        output_file.write(f"   \u274CGiven Answer: {given_answer_text} - INCORRECT\n")
                else:
                    answers = question.find_all('div', class_='answer')
                    option_counter = 1
                    for answer in answers:
                        match_left = answer.find('div', class_='answer_match_left')
                        match_right = answer.find('select')
                        correct_span = answer.find('span', class_='answer_arrow correct')
                        correct_points = points_awarded_numeric/points_possible_numeric
                        # if correct_points == 1 or correct_span is not None:
                        if correct_points == 1:
                            is_correct = True
                        elif correct_points <1:
                            is_correct = False
                        elif correct_span is not None:
                            is_correct = True

                        if match_left and match_right:
                            prompt = match_left.get_text(strip=True).replace('\u00A0', ' ')
                            selected_option = match_right.find('option', selected=True)
                            selected_text = selected_option.get_text(strip=True) if selected_option else "Not selected"
                            if is_correct:
                                output_file.write(f"   \u2714 Option {option_counter}: {prompt} {selected_text} - CORRECT\n")
                            else:
                                output_file.write(f"   \u274C Option {option_counter}: {prompt} {selected_text} - INCORRECT\n")
                        else:
                            answer_text_div = answer.find('div', class_='answer_text')
                            if answer_text_div:
                                answer_text = answer_text_div.get_text(strip=True).replace('\u00A0', ' ')
                                is_selected = 'selected_answer' in answer.get('class', [])
                                if is_selected:
                                    if is_correct:
                                        output_file.write(f"   \u2714 Option {option_counter}: {answer_text} - CORRECT\n")
                                    else:
                                        output_file.write(f"   \u274C Option {option_counter}: {answer_text} - SELECTED INCORRECT\n")
                                else:
                                    output_file.write(f"   Option {option_counter}: {answer_text}\n")

                        option_counter += 1

            else:
                output_file.write(f"{'-' * 40}\n")
                output_file.write(f"Question {question_index}:\n")
                output_file.write(f"{question_text}\n")
                output_file.write("Points information not available.\n")

            output_file.write(f"{'-' * 40}\n")

def BeforeAnswerWrapper_process_taken_quiz(file_path, output_file_name, quiz_number, class_name):
    
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
                output_file.write(f"{'✔ CORRECT' if is_correct else '✖ INCORRECT'} - {points_awarded}/{points_possible}pts\n")
                output_file.write(f"{question_text}\n")

                # Handle special types (numerical, matching, multiple-choice)
                given_answer_div = question.find('div', class_='form-control numerical-question-holder')
                if given_answer_div:
                    given_answer_input = given_answer_div.find('input', type='text')
                    given_answer_text = given_answer_input.get('value', '').strip() if given_answer_input else "NO ANSWER GIVEN"
                    if not given_answer_text:
                        given_answer_text = "NO ANSWER GIVEN"
                    output_file.write(f"   {'✔' if is_correct else '✖'} Given Answer: {given_answer_text}\n")
                else:
                    answers = question.find_all('div', class_='answer')
                    for idx, answer in enumerate(answers, 1):
                        match_left = answer.find('div', class_='answer_match_left')
                        match_right = answer.find('select')
                        correct_span = answer.find('span', class_='answer_arrow correct')
                        is_selected = 'selected_answer' in answer.get('class', [])

                        if match_left and match_right:
                            prompt = match_left.get_text(strip=True).replace('\u00A0', ' ')
                            selected_option = match_right.find('option', selected=True)
                            selected_text = selected_option.get_text(strip=True) if selected_option else "Not selected"
                            output_file.write(f"   {'✔' if is_correct else '✖'} Option {idx}: {prompt} {selected_text}\n")
                        else:
                            answer_text_div = answer.find('div', class_='answer_text')
                            if answer_text_div:
                                answer_text = answer_text_div.get_text(strip=True).replace('\u00A0', ' ')
                                if is_selected:
                                    output_file.write(f"   {'✔' if is_correct else '✖'} Option {idx}: {answer_text} (Selected)\n")
                                else:
                                    output_file.write(f"   Option {idx}: {answer_text}\n")

            else:
                output_file.write(f"{'-' * 40}\n")
                output_file.write(f"{question_number}:\n")
                output_file.write(f"{question_text}\n")
                output_file.write("Points information not available.\n")

            output_file.write(f"{'-' * 40}\n")
