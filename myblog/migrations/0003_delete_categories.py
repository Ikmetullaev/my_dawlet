# Generated by Django 4.2.5 on 2023-11-20 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_categories'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categories',
        ),
    ]
