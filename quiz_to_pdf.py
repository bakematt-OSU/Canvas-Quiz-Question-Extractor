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
    # OPEN THE TARGET MARKDOWN FILE FOR WRITING
    with open(output_path, "w", encoding="utf-8") as f:
        # WRITE THE QUIZ TITLE AS A MARKDOWN HEADING
        f.write(f"# Quiz: {quiz.title}\n\n")

        # ITERATE THROUGH EACH QUESTION IN THE QUIZ
        for question in quiz.questions:
            # WRITE THE QUESTION NUMBER AND TEXT AS A SUBHEADING
            f.write(f"## {question.number}: {question.text}\n")

            # EMBED EACH ASSOCIATED IMAGE FOR THE QUESTION
            for img in question.images:
                f.write(f"![Question Image]({img})\n")

            # DISPLAY EACH ANSWER OPTION WITH A CHECKBOX-LIKE MARK
            for option in question.options:
                mark = "[x]" if option.is_selected else "[ ]"
                f.write(f"- {mark} {option.text}\n")

                # EMBED EACH IMAGE ASSOCIATED WITH THE OPTION
                for img in option.images:
                    f.write(f"  ![Option Image]({img})\n")

            # ADD A LINE BREAK BETWEEN QUESTIONS
            f.write("\n")

    # PRINT CONFIRMATION MESSAGE TO CONSOLE
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
    # OPEN THE TARGET TEXT FILE FOR WRITING
    with open(output_path, "w", encoding="utf-8") as f:
        # WRITE THE QUIZ TITLE TO THE TOP OF THE FILE
        f.write(f"Quiz: {quiz.title}\n\n")

        # ITERATE THROUGH EACH QUESTION IN THE QUIZ
        for question in quiz.questions:
            # WRITE THE QUESTION NUMBER AND TEXT
            f.write(f"{question.number}: {question.text}\n")

            # WRITE EACH ANSWER OPTION WITH INDENTATION AND MARK
            for option in question.options:
                mark = "[x]" if option.is_selected else "[ ]"
                f.write(f"  {mark} {option.text}\n")

            # ADD A LINE BREAK BETWEEN QUESTIONS
            f.write("\n")

    # PRINT CONFIRMATION MESSAGE TO CONSOLE
    print(f"✅ Text file saved to {output_path}")
