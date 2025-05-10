from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict

@dataclass
class AnswerOption:
    text: str
    is_selected: bool = False
    is_correct: Optional[bool] = None
    images: List[str] = field(default_factory=list)

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(data):
        return AnswerOption(**data)

@dataclass
class Question:
    number: str
    text: str
    options: List[AnswerOption] = field(default_factory=list)
    is_correct: Optional[bool] = None
    points_awarded: Optional[float] = None
    points_possible: Optional[float] = None
    answer_given: Optional[str] = None
    matching_pairs: List[str] = field(default_factory=list)
    images: List[str] = field(default_factory=list)

    def to_dict(self):
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
    def from_dict(data):
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

@dataclass
class Quiz:
    title: str
    questions: List[Question] = field(default_factory=list)

    @property
    def total_points(self) -> float:
        return sum(q.points_possible or 0 for q in self.questions)

    @property
    def score(self) -> float:
        return sum(q.points_awarded or 0 for q in self.questions)

    def to_dict(self) -> Dict:
        return {
            "title": self.title,
            "questions": [q.to_dict() for q in self.questions]
        }

    @staticmethod
    def from_dict(data: Dict):
        return Quiz(
            title=data["title"],
            questions=[Question.from_dict(q) for q in data["questions"]]
        )
