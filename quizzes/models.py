from django.db import models


# Models list:
class Quiz(models.Model): ...
class Question(models.Model): ...
class Answer(models.Model): ...


class Quiz(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)


class Question(models.Model):
    text = models.CharField(max_length=512)
    test = models.ForeignKey(to=Quiz, on_delete=models.CASCADE,
                             related_name='questions')
    # right_answer = models.ForeignKey(to=Answer, on_delete=models.CASCADE,
    #                                  related_name='question2')
    # right_answer = models.OneToOneField(to='Answer', on_delete=models.CASCADE,
    #                                     related_name='right_for_question')
    # right_answer = models.ForeignKey(to='quizzes.Answer', on_delete=models.CASCADE,
    #                                  related_name='questions')
    # right_answer = models.IntegerField()
    price = models.IntegerField(default=0)


class Answer(models.Model):
    text = models.CharField(max_length=512)
    question = models.ForeignKey(to='Question', on_delete=models.CASCADE,
                                 related_name='answers')
    

class QuestionAnswer(models.Model):
    """ Right answers for each question """
    question = models.OneToOneField(to=Question, on_delete=models.CASCADE,
                                    related_name='right_answer')
    answer = models.ForeignKey(to=Answer, on_delete=models.CASCADE,
                               related_name='questions')
    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('question', 'answer'),
                name='right_answers'
            ),
        )