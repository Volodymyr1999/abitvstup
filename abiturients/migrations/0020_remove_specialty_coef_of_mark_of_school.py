# Generated by Django 2.1.7 on 2019-04-23 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abiturients', '0019_auto_20190423_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialty',
            name='coef_of_mark_of_school',
        ),
    ]
