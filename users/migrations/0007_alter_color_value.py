# Generated by Django 4.2.14 on 2024-07-16 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_user_passed_tests_user_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='value',
            field=models.CharField(default='rgba(0,0,0,1)', max_length=64),
        ),
    ]