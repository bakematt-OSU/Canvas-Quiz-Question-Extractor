from bs4 import BeautifulSoup
import os
import shutil
from typing import List
from quiz_models import Quiz, Question, AnswerOption

# OUTPUT FOLDER WHERE COPIED IMAGE FILES WILL BE STORED
IMAGE_OUTPUT_FOLDER = "_contents_library"

def extract_images_from_soup(soup_element, html_dir) -> List[str]:
    """
    EXTRACT AND COPY ALL <IMG> TAGS FROM A GIVEN SOUP ELEMENT,
    COPYING REFERENCED FILES TO THE IMAGE OUTPUT FOLDER.

    Args:
        soup_element (bs4.element.Tag): A BeautifulSoup object or subelement to search for <img> tags.
        html_dir (str): Directory path of the original HTML file for resolving relative image paths.

    Returns:
        List[str]: A list of destination file paths to the copied images.
    """
    image_paths = []

    # RETURN EARLY IF NO SOUP ELEMENT IS PROVIDED
    if not soup_element:
        return image_paths

    # ENSURE THE IMAGE OUTPUT FOLDER EXISTS
    os.makedirs(IMAGE_OUTPUT_FOLDER, exist_ok=True)

    # FIND ALL <IMG> TAGS INSIDE THE SOUP ELEMENT
    for img in soup_element.find_all("img"):
        src = img.get("src")
        if src:
            # BUILD SOURCE PATH (HANDLE RELATIVE VS ABSOLUTE)
            img_path = os.path.join(html_dir, src) if not os.path.isabs(src) else src
            filename = os.path.basename(src)
            dest_path = os.path.join(IMAGE_OUTPUT_FOLDER, filename)
            try:
                # COPY IMAGE FILE TO DESTINATION FOLDER
                shutil.copy(img_path, dest_path)
                image_paths.append(dest_path)
            except Exception as e:
                # WARN IF COPY FAILS
                print(f"WARNING: FAILED TO COPY IMAGE: {img_path} -> {dest_path}: {e}")

    return image_paths

def parse_quiz_html(file_path: str, quiz_title: str = "UNTITLED QUIZ") -> Quiz:
    """
    PARSE A CANVAS-STYLE HTML QUIZ EXPORT INTO A Quiz OBJECT.

    Args:
        file_path (str): Full path to the HTML quiz file.
        quiz_title (str): Optional title for the resulting Quiz object.

    Returns:
        Quiz: A Quiz object populated with extracted questions and answer options.
    """
    # OPEN AND PARSE THE HTML FILE
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # GET DIRECTORY TO RESOLVE RELATIVE IMAGE PATHS
    html_dir = os.path.dirname(file_path)

    extracted_questions = []  # LIST TO STORE PARSED QUESTIONS

    # FIND ALL QUESTION BLOCKS
    question_divs = soup.find_all("div", class_="display_question")

    # ITERATE THROUGH EACH QUESTION BLOCK
    for q_idx, q_div in enumerate(question_divs, 1):
        question_number = f"Question {q_idx}"

        # EXTRACT QUESTION TEXT AND IMAGES
        question_text_div = q_div.find("div", class_="question_text")
        question_text = question_text_div.get_text(separator="\n", strip=True) if question_text_div else "No question text found."
        question_images = extract_images_from_soup(question_text_div, html_dir)

        options = []

        # EXTRACT ANSWER OPTIONS AND ASSOCIATED IMAGES
        answers_div = q_div.find("div", class_="answers")
        if answers_div:
            answer_divs = answers_div.find_all("div", class_="answer")
            for answer_div in answer_divs:
                label = answer_div.find("div", class_="answer_text")
                answer_text = label.get_text(strip=True) if label else "No answer text"
                images = extract_images_from_soup(answer_div, html_dir)
                is_selected = "selected_answer" in answer_div.get("class", [])
                options.append(AnswerOption(text=answer_text, is_selected=is_selected, images=images))

        # EXTRACT SCORE INFORMATION (IF PRESENT)
        points_awarded = points_possible = None
        user_points_div = q_div.find("div", class_="user_points")
        if user_points_div:
            try:
                score_parts = user_points_div.get_text(strip=True).split("/")
                points_awarded = float(score_parts[0])
                points_possible = float(score_parts[1].replace("pts", "").strip())
            except:
                # IGNORE PARSE ERRORS SILENTLY
                pass

        # CREATE A QUESTION OBJECT AND ADD TO LIST
        extracted_questions.append(Question(
            number=question_number,
            text=question_text,
            options=options,
            images=question_images,
            points_awarded=points_awarded,
            points_possible=points_possible
        ))

    # RETURN FINAL QUIZ OBJECT
    return Quiz(title=quiz_title, questions=extracted_questions)
