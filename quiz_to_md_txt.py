from quiz_models import Quiz
import os

def export_quiz_to_markdown(quiz: Quiz, output_path: str):
    """
    EXPORT A QUIZ OBJECT TO A MARKDOWN (.md) FILE FORMAT.

    Args:
        quiz (Quiz): The quiz object to export.
        output_path (str): Destination file path for the Markdown file.

    Returns:
        None
    """
    # OPEN FILE FOR WRITING WITH UTF-8 ENCODING
    with open(output_path, "w", encoding="utf-8") as f:
        # WRITE QUIZ TITLE
        f.write(f"# Quiz: {quiz.title}\n\n")

        # LOOP THROUGH EACH QUESTION IN THE QUIZ
        for question in quiz.questions:
            f.write(f"## {question.number}: {question.text}\n")

            # INCLUDE ANY IMAGES ASSOCIATED WITH THE QUESTION
            for img in question.images:
                f.write(f"![Question Image]({img})\n")

            # LIST ALL ANSWER OPTIONS
            for option in question.options:
                mark = "[x]" if option.is_selected else "[ ]"
                f.write(f"- {mark} {option.text}\n")

                # INCLUDE IMAGES ASSOCIATED WITH THE OPTION
                for img in option.images:
                    f.write(f"  ![Option Image]({img})\n")

            f.write("\n")  # ADD SPACING BETWEEN QUESTIONS

    # CONFIRM OUTPUT
    print(f"✅ Markdown saved to {output_path}")

def export_quiz_to_txt(quiz: Quiz, output_path: str):
    """
    EXPORT A QUIZ OBJECT TO A PLAIN TEXT (.txt) FILE FORMAT.

    Args:
        quiz (Quiz): The quiz object to export.
        output_path (str): Destination file path for the text file.

    Returns:
        None
    """
    # OPEN FILE FOR WRITING WITH UTF-8 ENCODING
    with open(output_path, "w", encoding="utf-8") as f:
        # WRITE QUIZ TITLE
        f.write(f"Quiz: {quiz.title}\n\n")

        # LOOP THROUGH EACH QUESTION IN THE QUIZ
        for question in quiz.questions:
            f.write(f"{question.number}: {question.text}\n")

            # LIST ALL ANSWER OPTIONS
            for option in question.options:
                mark = "[x]" if option.is_selected else "[ ]"
                f.write(f"  {mark} {option.text}\n")

            f.write("\n")  # ADD SPACING BETWEEN QUESTIONS

    # CONFIRM OUTPUT
    print(f"✅ Text file saved to {output_path}")
