# ---------------------------------------------------
# QUIZ EXTRACTOR WITH STRUCTURED DATA CLASSES AND IMAGE SUPPORT
# ---------------------------------------------------

from dataclasses import dataclass, field  # PROVIDES A DECORATOR AND FUNCTIONS FOR DEFINING DATA CLASSES
from typing import List, Optional         # PROVIDES SUPPORT FOR OPTIONAL TYPING AND LISTS
from bs4 import BeautifulSoup             # HTML PARSER FOR EXTRACTING QUIZ CONTENT
import os                                 # OS UTILITIES
import shutil                             # USED FOR COPYING IMAGE FILES

INPUT_FOLDER = "Input"                    # FOLDER CONTAINING HTML INPUT FILES
IMAGE_OUTPUT_FOLDER = "_contents_library" # DESTINATION FOR COPIED IMAGE FILES

@dataclass
class AnswerOption:
    """
    REPRESENTS A SINGLE ANSWER OPTION WITHIN A QUIZ QUESTION.
    """
    text: str
    is_selected: bool = False
    is_correct: Optional[bool] = None
    images: List[str] = field(default_factory=list)

@dataclass
class Question:
    """
    REPRESENTS A QUIZ QUESTION WITH ALL ASSOCIATED METADATA.
    """
    number: str
    text: str
    options: List[AnswerOption] = field(default_factory=list)
    is_correct: Optional[bool] = None
    points_awarded: Optional[float] = None
    points_possible: Optional[float] = None
    answer_given: Optional[str] = None
    matching_pairs: List[str] = field(default_factory=list)
    images: List[str] = field(default_factory=list)

@dataclass
class Quiz:
    """
    REPRESENTS A FULL QUIZ INCLUDING ALL QUESTIONS AND TOTAL SCORE.
    """
    title: str
    questions: List[Question] = field(default_factory=list)

    @property
    def total_points(self) -> float:
        # CALCULATES TOTAL POSSIBLE POINTS FOR THE QUIZ
        return sum(q.points_possible or 0 for q in self.questions)

    @property
    def score(self) -> float:
        # CALCULATES TOTAL AWARDED POINTS FOR THE QUIZ
        return sum(q.points_awarded or 0 for q in self.questions)

def extract_images_from_soup(soup_element, html_dir) -> List[str]:
    """
    Extracts image file paths from HTML and copies them to the _contents_library folder,
    while logging missing or failed image paths.

    Args:
        soup_element (BeautifulSoup element): The HTML element to search for images.
        html_dir (str): The base directory where the HTML file and images are located.

    Returns:
        List[str]: A list of paths to the successfully copied images.
    """
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

            if not os.path.exists(img_path):
                print(f"[MISSING] Image not found: {img_path}")
                continue

            try:
                shutil.copy(img_path, dest_path)
                print(f"[COPIED] {img_path} -> {dest_path}")
                image_paths.append(dest_path)
            except Exception as e:
                print(f"[ERROR] Failed to copy image: {img_path} -> {dest_path}: {e}")

    return image_paths



# def extract_images_from_soup(soup_element, html_dir) -> List[str]:
#     """
#     EXTRACTS IMAGE URLS FROM HTML AND COPIES IMAGES TO THE _CONTENTS_LIBRARY FOLDER.
#     """
#     image_paths = []
#     if not soup_element:
#         return image_paths

#     os.makedirs(IMAGE_OUTPUT_FOLDER, exist_ok=True)  # ENSURE OUTPUT FOLDER EXISTS

#     for img in soup_element.find_all("img"):  # LOOP THROUGH ALL IMG TAGS
#         src = img.get("src")  # GET IMAGE SRC ATTRIBUTE
#         if src:
#             img_path = os.path.join(html_dir, src) if not os.path.isabs(src) else src  # RESOLVE IMAGE PATH
#             filename = os.path.basename(src)  # GET FILENAME FROM SRC
#             dest_path = os.path.join(IMAGE_OUTPUT_FOLDER, filename)  # BUILD DESTINATION PATH
#             try:
#                 shutil.copy(img_path, dest_path)  # COPY IMAGE FILE
#                 image_paths.append(dest_path)  # STORE DESTINATION PATH
#             except Exception as e:
#                 print(f"WARNING: FAILED TO COPY IMAGE: {img_path} -> {dest_path}: {e}")  # LOG ERROR

#     return image_paths  # RETURN LIST OF COPIED IMAGE PATHS

def parse_quiz_html(file_path: str, quiz_title: str = "UNTITLED QUIZ") -> Quiz:
    """
    PARSES A CANVAS-STYLE HTML QUIZ FILE AND RETURNS A STRUCTURED QUIZ OBJECT.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")  # PARSE HTML FILE

    html_dir = os.path.dirname(file_path)  # DETERMINE DIRECTORY OF HTML FILE
    extracted_questions = []  # LIST TO STORE PARSED QUESTIONS
    question_divs = soup.find_all("div", class_="display_question")  # FIND ALL QUESTION DIVS

    for q_idx, q_div in enumerate(question_divs, 1):
        question_number = f"Question {q_idx}"  # GENERATE QUESTION NUMBER

        # EXTRACT QUESTION TEXT AND IMAGES
        question_text_div = q_div.find("div", class_="question_text")
        question_text = question_text_div.get_text(separator="\n", strip=True) if question_text_div else "No question text found."
        question_images = extract_images_from_soup(question_text_div, html_dir)

        # EXTRACT ANSWER OPTIONS
        options = []
        answers_div = q_div.find("div", class_="answers")
        if answers_div:
            answer_divs = answers_div.find_all("div", class_="answer")  # GET ALL ANSWER CHOICES
            for answer_div in answer_divs:
                label = answer_div.find("div", class_="answer_text")  # FIND THE TEXT LABEL
                answer_text = label.get_text(strip=True) if label else "No answer text"
                images = extract_images_from_soup(answer_div, html_dir)  # EXTRACT IMAGES FOR THIS OPTION
                is_selected = "selected_answer" in answer_div.get("class", [])  # DETERMINE IF SELECTED
                options.append(AnswerOption(text=answer_text, is_selected=is_selected, images=images))  # CREATE OPTION

        # EXTRACT POINTS AWARDED AND POSSIBLE
        points_awarded = points_possible = None
        user_points_div = q_div.find("div", class_="user_points")
        if user_points_div:
            try:
                score_parts = user_points_div.get_text(strip=True).split("/")  # SPLIT "X / Y" FORMAT
                points_awarded = float(score_parts[0])  # PARSE AWARDED POINTS
                points_possible = float(score_parts[1].replace("pts", "").strip())  # PARSE POSSIBLE POINTS
            except:
                pass  # IGNORE ANY PARSE ERRORS

        # CREATE AND ADD QUESTION OBJECT
        extracted_questions.append(Question(
            number=question_number,
            text=question_text,
            options=options,
            images=question_images,
            points_awarded=points_awarded,
            points_possible=points_possible
        ))

    return Quiz(title=quiz_title, questions=extracted_questions)  # RETURN QUIZ OBJECT
