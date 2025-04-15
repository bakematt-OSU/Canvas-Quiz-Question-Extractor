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
            answers = question.find_all('div', class_='answer')

            output_file.write(f"----------------------------------------\nQuestion {question_index}:\n")
            output_file.write(f"{question_text}\n")

            # Track whether there are selected answers and unselected answers
            selected_answers = []
            unselected_answers = []

            for idx, answer in enumerate(answers, 1):
                # Check if the answer text exists before trying to extract it
                answer_text_tag = answer.find('div', class_='answer_text')
                
                # If the answer text exists, extract it, else set it to 'No Answer'
                answer_text = answer_text_tag.get_text(strip=True) if answer_text_tag else 'No Answer'
                is_correct = 'correct' in answer.get('class', [])
                is_selected = 'selected_answer' in answer.get('class', [])

                # Collect selected and unselected answers
                if is_selected:
                    selected_answers.append(f"  ✔ Option {idx}: {answer_text} - Correct")
                else:
                    unselected_answers.append(f"  ❌ Option {idx}: {answer_text} - Incorrect")

            # Write selected answers first
            for selected in selected_answers:
                output_file.write(f"{selected}\n")

            # Then write unselected answers
            for unselected in unselected_answers:
                output_file.write(f"{unselected}\n")

            output_file.write("----------------------------------------\n")
