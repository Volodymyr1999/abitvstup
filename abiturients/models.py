from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Region(models.Model):
    Region_name = models.CharField(max_length=100)

    def __str__(self):
        return "{0} {1}".format(self.id,self.Region_name)




class VNZ(models.Model):
    name = models.CharField(max_length=500)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}".format(self.name)


class Specialty(models.Model):
    name_of_specialty = models.CharField(max_length=250)


    steps = (
        ('B','Бакалавр'),
        ('M','Магістр'),

    )
    step = models.CharField(max_length=10,choices=steps, default='B')

    count_of_abiturients = models.PositiveIntegerField()
    count_of_contract_abiturients = models.PositiveIntegerField(default=0)
    vnz = models.ManyToManyField(VNZ)
    forms = (
        ('day', 'денна'),
        ('part-time', 'заочна'),
        ('afternoon', 'вечірня')
    )

    form  = models.CharField(max_length=20,choices=forms)
    students = models.ManyToManyField('Abiturient_Statement')
    def __str__(self):
        return '{0}'.format(self.name_of_specialty)


class Subject(models.Model):
    name_of_subject = models.CharField(max_length=250)
    coef = models.FloatField(default=0.1)
    mark = models.IntegerField(default=100,null=True)
    specialty = models.ManyToManyField(Specialty)

    def __str__(self):
        return "{0}".format(self.name_of_subject)


class Abiturient_Statement(models.Model):
    username = models.CharField(max_length=80)
    priority = models.CharField(max_length=10)
    mark = models.FloatField()
    status = models.CharField(max_length=100,null=True)
    isdocument = models.CharField(max_length=1, default='+')
    vnzs = models.ManyToManyField(VNZ)


    def __str__(self):
        return "{0}".format(self.username)


