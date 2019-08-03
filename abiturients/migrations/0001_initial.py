# Generated by Django 2.1.7 on 2019-04-15 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abiturient_Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('priority', models.SmallIntegerField()),
                ('mark_from_school', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Region_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_specialty', models.CharField(max_length=100)),
                ('faculty', models.CharField(max_length=100)),
                ('type_of_science', models.CharField(max_length=200)),
                ('step', models.CharField(choices=[('Bachelor', 'Бакалавр'), ('Master', 'Магістр')], default='Bachelor', max_length=10)),
                ('count_of_abiturients', models.PositiveIntegerField()),
                ('count_of_contract_abiturients', models.PositiveIntegerField(default=0)),
                ('coef_of_mark_of_school', models.FloatField(default=0.1)),
                ('form', models.CharField(choices=[('day', 'денна'), ('part-time', 'заочна'), ('afternoon', 'вечірня')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_subject', models.CharField(max_length=50)),
                ('coef', models.FloatField(default=0.1)),
                ('mark', models.IntegerField(default=100)),
                ('specialty', models.ManyToManyField(to='abiturients.Specialty')),
            ],
        ),
        migrations.CreateModel(
            name='VNZ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('private', models.BooleanField(default=False)),
                ('rector', models.CharField(max_length=50)),
                ('post_index', models.PositiveSmallIntegerField(max_length=6)),
                ('adress', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=13)),
                ('web_site', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abiturients.Region')),
            ],
        ),
        migrations.AddField(
            model_name='abiturient_statement',
            name='subjects',
            field=models.ManyToManyField(to='abiturients.Subject'),
        ),
    ]