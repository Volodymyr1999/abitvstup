# Generated by Django 2.1.7 on 2019-04-23 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abiturients', '0021_specialty_vnz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='mark',
            field=models.IntegerField(default=100, null=True),
        ),
    ]
