# Generated by Django 2.1.7 on 2019-04-15 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abiturients', '0010_remove_vnz_adress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vnz',
            name='post_index',
            field=models.CharField(max_length=10),
        ),
    ]