# Generated by Django 4.2.14 on 2024-07-15 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_initial'),
        ('users', '0004_user_colors'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='passed_tests',
            field=models.ManyToManyField(to='quizzes.quiz'),
        ),
    ]
