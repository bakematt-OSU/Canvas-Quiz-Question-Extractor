from quiz_models import Quiz
import os

def export_quiz_to_markdown(quiz: Quiz, output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# Quiz: {quiz.title}\n\n")
        for question in quiz.questions:
            f.write(f"## {question.number}: {question.text}\n")

            for img in question.images:
                f.write(f"![Question Image]({img})\n")

            for option in question.options:
                mark = "[x]" if option.is_selected else "[ ]"
                f.write(f"- {mark} {option.text}\n")
                for img in option.images:
                    f.write(f"  ![Option Image]({img})\n")

            f.write("\n")

    print(f"✅ Markdown saved to {output_path}")

def export_quiz_to_txt(quiz: Quiz, output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"Quiz: {quiz.title}\n\n")
        for question in quiz.questions:
            f.write(f"{question.number}: {question.text}\n")

            for option in question.options:
                mark = "[x]" if option.is_selected else "[ ]"
                f.write(f"  {mark} {option.text}\n")

            f.write("\n")

    print(f"✅ Text file saved to {output_path}")
