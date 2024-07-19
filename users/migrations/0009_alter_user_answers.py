# Generated by Django 4.2.14 on 2024-07-19 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0007_rename_price_question_points'),
        ('users', '0008_remove_user_passed_tests_number_alter_color_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='answers',
            field=models.ManyToManyField(null=True, to='quizzes.answer'),
        ),
    ]
