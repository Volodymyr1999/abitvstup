# Generated by Django 2.1.7 on 2019-04-15 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abiturients', '0005_auto_20190416_0020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vnz',
            name='email',
        ),
    ]
