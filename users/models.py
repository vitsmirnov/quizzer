from django.db import models
from django.contrib.auth.models import AbstractUser

from quizzes.models import Quiz, Answer


# from django.conf import settings
# from django.contrib.auth import get_user_modelf
# settings.AUTH_USER_MODEL


class Color(models.Model):
    name = models.CharField(verbose_name='Color name', default='', unique=True,
                            max_length=32)
    value = models.CharField(default='rgba(255,255,255,1)', max_length=64)  # unique=?
    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"Color: {self.name} ({self.value}), price: {self.price}"


class User(AbstractUser):
    balance = models.IntegerField(default=0)
    color = models.ForeignKey(to=Color, on_delete=models.CASCADE,
        related_name='users', null=True, blank=True)  # default= ?
    
    colors = models.ManyToManyField(Color)
    # User's answers for quiz questions (statistics)
    answers = models.ManyToManyField(Answer)
    # Working with answers like that is probably not optimal
    # and we should create a table for statistics or something like that:
    # passed_quizzees = models.ManyToManyField(Quiz)  # ?!
    # but maybe not..

    def is_quiz_passed(self, quiz_id: int) -> bool:
        for answer in self.answers.all():
            if answer.question.quiz.id == quiz_id:
                return True
        return False
    
    def passed_quizzes(self) -> set[Quiz]:
        result = set()
        for answer in self.answers.all():
            result.add(answer.question.quiz)
        return result
    
    @property
    def passed_quizzes_count(self) -> int:
        return len(self.passed_quizzes())
    
    def quiz_answers(self, quiz_id: int) -> list[Answer]:
        """ It returns the answers for particular quiz """
        result = list()
        for answer in self.answers.all():
            if answer.question.quiz.id == quiz_id:
                result.append(answer)
        return result
    
    # temp (for degugging)
    def _print_passed_quizzes(self) -> None:
        quizzes = self.passed_quizzes()
        for quiz in quizzes:
            print(quiz)
            for question in quiz.questions.all():
                print(f'\t{ question }')
                for answer in question.answers.all():
                    print(f'\t\t{ answer }')
                print(f'\t\t->\t{ question.right_answer }')
                # user's answer
                # There is no any difference between filter() and get in terms of query execution speed.
                print(f'\t\tu ->\t{ self.answers.filter(question__id=question.id).first() }')
