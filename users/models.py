from django.db import models
from django.contrib.auth.models import AbstractUser

from quizzes.models import Quiz, Answer

# from colorfield.fields import ColorField


# from django.conf import settings
# settings.AUTH_USER_MODEL
# get_user_model()

# Create your models here.

# class User: ...
# class Color: ...


class Color(models.Model):
    name = models.CharField(verbose_name='Color name', default='', unique=True,
                            max_length=32)
    value = models.IntegerField(default=0, unique=True) # str?
    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"Color: {self.name} ({self.value}), price: {self.price}"


class User(AbstractUser):
    balance = models.IntegerField(default=0)
    color = models.ForeignKey(to=Color, on_delete=models.CASCADE,
                              related_name='users', null=True, blank=True)
    passed_tests_number = models.IntegerField(default=0)

    colors = models.ManyToManyField(Color)
    answers = models.ManyToManyField(Answer)
    # passed_quizzees = models.ManyToManyField(Quiz)  # ?!

    def __str__(self) -> str:
        return super().__str__() + f" balance: {self.balance}"
    
    def is_quiz_passed(self, quiz_id: int, quiz: Quiz=None) -> bool:  # quiz_id: int
        print(quiz)
        print(self.answers.all())
        for answer in self.answers.all():
            print(answer.question.quiz == quiz)
            if answer.question.quiz == quiz:
                return True
        return False
