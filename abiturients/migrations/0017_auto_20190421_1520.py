# Generated by Django 2.1.7 on 2019-04-21 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abiturients', '0016_auto_20190421_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vnz',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]