# Generated by Django 2.1.7 on 2019-05-08 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abiturients', '0023_auto_20190423_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abiturient_statement',
            old_name='mark_from_school',
            new_name='mark',
        ),
        migrations.RemoveField(
            model_name='abiturient_statement',
            name='subjects',
        ),
        migrations.AddField(
            model_name='abiturient_statement',
            name='isdocument',
            field=models.CharField(default='+', max_length=1),
        ),
        migrations.AddField(
            model_name='abiturient_statement',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='abiturient_statement',
            name='priority',
            field=models.CharField(max_length=10),
        ),
    ]
