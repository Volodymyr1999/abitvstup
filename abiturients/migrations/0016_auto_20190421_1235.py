# Generated by Django 2.1.7 on 2019-04-21 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abiturients', '0015_auto_20190421_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialty',
            name='step',
            field=models.CharField(choices=[('Bachelor', 'Бакалавр'), ('Master', 'Магістр'), ('Younger', 'Молодший')], default='Bachelor', max_length=10),
        ),
    ]