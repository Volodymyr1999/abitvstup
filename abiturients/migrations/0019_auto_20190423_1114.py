# Generated by Django 2.1.7 on 2019-04-23 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abiturients', '0018_auto_20190423_0859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialty',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='specialty',
            name='type_of_science',
        ),
    ]