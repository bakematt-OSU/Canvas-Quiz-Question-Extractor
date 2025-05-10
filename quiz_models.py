from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict

# DATA CLASS TO REPRESENT AN INDIVIDUAL ANSWER OPTION
@dataclass
class AnswerOption:
    """
    REPRESENTS A SINGLE ANSWER OPTION FOR A QUESTION.

    Attributes:
        text (str): The answer text.
        is_selected (bool): Whether the option was selected by the user.
        is_correct (Optional[bool]): Whether the option is correct.
        images (List[str]): Associated image file paths (if any).
    """
    text: str
    is_selected: bool = False
    is_correct: Optional[bool] = None
    images: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        """
        CONVERT THE ANSWER OPTION TO A DICTIONARY.

        Returns:
            dict: Serializable dictionary representation.
        """
        return asdict(self)

    @staticmethod
    def from_dict(data: Dict) -> 'AnswerOption':
        """
        CREATE AN ANSWER OPTION INSTANCE FROM A DICTIONARY.

        Args:
            data (dict): Dictionary with answer option fields.

        Returns:
            AnswerOption: New instance of AnswerOption.
        """
        return AnswerOption(**data)

# DATA CLASS TO REPRESENT A QUIZ QUESTION
@dataclass
class Question:
    """
    REPRESENTS A SINGLE QUESTION IN A QUIZ.

    Attributes:
        number (str): The question number or identifier.
        text (str): The main question text.
        options (List[AnswerOption]): List of possible answer options.
        is_correct (Optional[bool]): Whether the user's answer is fully correct.
        points_awarded (Optional[float]): Points received by the user.
        points_possible (Optional[float]): Maximum points available.
        answer_given (Optional[str]): Raw answer input or selection.
        matching_pairs (List[str]): For matching-style questions.
        images (List[str]): Associated image file paths.
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

    def to_dict(self) -> Dict:
        """
        CONVERT THE QUESTION TO A SERIALIZABLE DICTIONARY.

        Returns:
            dict: Dictionary representation of the question.
        """
        return {
            "number": self.number,
            "text": self.text,
            "options": [opt.to_dict() for opt in self.options],
            "is_correct": self.is_correct,
            "points_awarded": self.points_awarded,
            "points_possible": self.points_possible,
            "answer_given": self.answer_given,
            "matching_pairs": self.matching_pairs,
            "images": self.images
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Question':
        """
        CREATE A QUESTION INSTANCE FROM A DICTIONARY.

        Args:
            data (dict): Dictionary with question data.

        Returns:
            Question: New instance of Question.
        """
        return Question(
            number=data["number"],
            text=data["text"],
            options=[AnswerOption.from_dict(opt) for opt in data["options"]],
            is_correct=data.get("is_correct"),
            points_awarded=data.get("points_awarded"),
            points_possible=data.get("points_possible"),
            answer_given=data.get("answer_given"),
            matching_pairs=data.get("matching_pairs", []),
            images=data.get("images", [])
        )

# DATA CLASS TO REPRESENT A FULL QUIZ
@dataclass
class Quiz:
    """
    REPRESENTS A FULL QUIZ WITH QUESTIONS AND METADATA.

    Attributes:
        title (str): The quiz title.
        questions (List[Question]): List of questions in the quiz.
    """
    title: str
    questions: List[Question] = field(default_factory=list)

    @property
    def total_points(self) -> float:
        """
        CALCULATE THE TOTAL POSSIBLE POINTS FOR THE QUIZ.

        Returns:
            float: Sum of points_possible from all questions.
        """
        return sum(q.points_possible or 0 for q in self.questions)

    @property
    def score(self) -> float:
        """
        CALCULATE THE TOTAL SCORE OBTAINED.

        Returns:
            float: Sum of points_awarded from all questions.
        """
        return sum(q.points_awarded or 0 for q in self.questions)

    def to_dict(self) -> Dict:
        """
        CONVERT THE QUIZ TO A DICTIONARY FORMAT.

        Returns:
            dict: Serializable dictionary of quiz data.
        """
        return {
            "title": self.title,
            "questions": [q.to_dict() for q in self.questions]
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Quiz':
        """
        CREATE A QUIZ INSTANCE FROM A DICTIONARY.

        Args:
            data (dict): Dictionary with quiz fields.

        Returns:
            Quiz: New instance of Quiz.
        """
        return Quiz(
            title=data["title"],
            questions=[Question.from_dict(q) for q in data["questions"]]
        )
