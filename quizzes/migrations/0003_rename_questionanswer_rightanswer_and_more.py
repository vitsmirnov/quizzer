# Generated by Django 4.2.14 on 2024-07-16 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_questionanswer_questionanswer_right_answers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuestionAnswer',
            new_name='RightAnswer',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='test',
            new_name='quiz',
        ),
    ]