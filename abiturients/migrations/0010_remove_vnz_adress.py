# Generated by Django 2.1.7 on 2019-04-15 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abiturients', '0009_auto_20190416_0216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vnz',
            name='adress',
        ),
    ]
