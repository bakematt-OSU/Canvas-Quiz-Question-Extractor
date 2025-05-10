from bs4 import BeautifulSoup
import os
import shutil
from typing import List
from quiz_models import Quiz, Question, AnswerOption

IMAGE_OUTPUT_FOLDER = "_contents_library"

def extract_images_from_soup(soup_element, html_dir) -> List[str]:
    image_paths = []
    if not soup_element:
        return image_paths

    os.makedirs(IMAGE_OUTPUT_FOLDER, exist_ok=True)

    for img in soup_element.find_all("img"):
        src = img.get("src")
        if src:
            img_path = os.path.join(html_dir, src) if not os.path.isabs(src) else src
            filename = os.path.basename(src)
            dest_path = os.path.join(IMAGE_OUTPUT_FOLDER, filename)
            try:
                shutil.copy(img_path, dest_path)
                image_paths.append(dest_path)
            except Exception as e:
                print(f"WARNING: FAILED TO COPY IMAGE: {img_path} -> {dest_path}: {e}")

    return image_paths

def parse_quiz_html(file_path: str, quiz_title: str = "UNTITLED QUIZ") -> Quiz:
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    html_dir = os.path.dirname(file_path)
    extracted_questions = []
    question_divs = soup.find_all("div", class_="display_question")

    for q_idx, q_div in enumerate(question_divs, 1):
        question_number = f"Question {q_idx}"
        question_text_div = q_div.find("div", class_="question_text")
        question_text = question_text_div.get_text(separator="\n", strip=True) if question_text_div else "No question text found."
        question_images = extract_images_from_soup(question_text_div, html_dir)

        options = []
        answers_div = q_div.find("div", class_="answers")
        if answers_div:
            answer_divs = answers_div.find_all("div", class_="answer")
            for answer_div in answer_divs:
                label = answer_div.find("div", class_="answer_text")
                answer_text = label.get_text(strip=True) if label else "No answer text"
                images = extract_images_from_soup(answer_div, html_dir)
                is_selected = "selected_answer" in answer_div.get("class", [])
                options.append(AnswerOption(text=answer_text, is_selected=is_selected, images=images))

        points_awarded = points_possible = None
        user_points_div = q_div.find("div", class_="user_points")
        if user_points_div:
            try:
                score_parts = user_points_div.get_text(strip=True).split("/")
                points_awarded = float(score_parts[0])
                points_possible = float(score_parts[1].replace("pts", "").strip())
            except:
                pass

        extracted_questions.append(Question(
            number=question_number,
            text=question_text,
            options=options,
            images=question_images,
            points_awarded=points_awarded,
            points_possible=points_possible
        ))

    return Quiz(title=quiz_title, questions=extracted_questions)
