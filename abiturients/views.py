from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse,JsonResponse
import csv
from .models import *
from django.views import generic
from django.db.models import Q,aggregates
from django.core import serializers
from collections import Counter
import math
import  multiprocessing
# Create your views here.


class RegionView(generic.ListView):
    model = Region
    template_name = "abiturients/index.html"

def VnzListView(request,pk):
    region = Region.objects.get(pk=pk)

    allvnzs = region.vnz_set.all().order_by('name')

    paginator = Paginator(allvnzs,25)

    page = request.GET.get('page')
    vnzs = paginator.get_page(page)
    return render(request,"abiturients/vnzs.html",{'vnzs': vnzs,'region':region})


def SpecListView(request,pk):
    vnz = VNZ.objects.get(pk=pk)

    specialties_set = vnz.specialty_set.order_by('name_of_specialty')

    paginator = Paginator(specialties_set,100)
    page = request.GET.get('page')
    specialties = paginator.get_page(page)

    return render(request,"abiturients/specialties.html",{'specialties':specialties,'vnz':vnz})


def SpecView(request,pk):
    specialty=Specialty.objects.get(pk=pk)
    studs = specialty.students.order_by(('-mark'))


    paginator = Paginator(studs,100)
    page = request.GET.get('page')
    students = paginator.get_page(page)

    return render(request,"abiturients/students.html",{'students':students,'specialty':specialty})




def get_statistic_for_region(request):
    pk = request.GET.get('pk')
    region = Region.objects.get(pk=pk)

    vnzs_count = region.vnz_set.count()
    univercities = region.vnz_set.filter(name__contains="університет").exclude(name__contains="коледж")\
        .exclude(name__contains="філія").exclude(name__contains="інститут")\
        .exclude(name__contains="пункт").exclude(name__contains="університету")

    academies = region.vnz_set.filter(name__contains="академія").exclude(name__contains="інститут")
    institutes = region.vnz_set.filter(name__contains="інститут").exclude(name__contains="коледж")\
        .exclude(name__contains="товариство")
    colleges = region.vnz_set.filter(Q(name__contains="коледж")|Q(name__contains="Коледж")).exclude(name__contains="філія")
    count = univercities.count()
    acount = academies.count()
    icount = institutes.count()
    colcount = colleges.count()
    elsecount=vnzs_count-(count+acount+icount+colcount)


    return JsonResponse({'ucount':count,'acount':acount,'icount':icount,'colcount':colcount,'elsecount':elsecount})




def get5Specilaties(request):
    pk=request.GET.get('pk')
    vnz=VNZ.objects.get(pk=pk)

    specilaties = list(vnz.specialty_set.annotate(counts=aggregates.Count('students')).order_by('-counts')[:5])
    specilaties.sort(key=lambda x: x.count_of_abiturients)
    specilaties = serializers.serialize('json',specilaties)
    data={
        "specs":specilaties
    }
    return JsonResponse(data)

def get10students(request):
    pk = request.GET.get('pk')

    spec=Specialty.objects.get(pk=pk)

    students = list(spec.students.order_by('-mark')[:10])
    students.sort(key=lambda x: x.username)
    # students = students.order_by('username')
    students = serializers.serialize('json',students)
    statistic_for_polygon(spec)
    data={
        'students': students
    }

    return JsonResponse(data)

def statistic_for_polygon(request):
    pk = request.GET.get('pk')

    spec = Specialty.objects.get(pk=pk)

    students = spec.students.order_by('mark')

    marks = [i.mark for i in students]


    n=len(marks)

    r = int(math.log(n,2))+1

    rozm = marks[-1]-marks[0]

    d=rozm/r
    s=marks[0]
    intervals=[]
    for i in range(r):
        intervals.append((s,s+d))
        s+=d

    middles=[]
    counts=[]
    for i in intervals:
        k=0
        for j in marks:
            if j>=i[0] and j<i[1]:
                k+=1
        middles.append(round((i[0]+i[1])/2,2))
        counts.append(k)

    data={
        'middles':middles,
        'counts':counts
    }

    return JsonResponse(data)



def doc(request):
    return render(request,'abiturients/doc.html')

def help(request):
    return render(request,'abiturients/file.html')











def Delete(request):


    for sp in Region.objects.all():
        for st in sp.vnz_set.all():
            st.delete()



    return HttpResponse('deleted')













def vns(request):
    vnzs = VNZ.objects.all()
    v=[]
    for i in vnzs:
        if i.specialty_set.count() != 0:
            v.append(i)

    return HttpResponse(len(v))

def readvnzs():

    with open("Vnz.csv",'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            region = Region.objects.get(Region_name=row['region'])

            vnz=VNZ.objects.create(name=row['vnz'],region=region)
            vnz.region = region


def addvnzs(request):

    readvnzs()

    return HttpResponse("succes")

def addspec(request):
    with open('st.csv','r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            vnz=VNZ.objects.filter(name=row['vnz'])
            count = 0
            kcount =0
            if row['count']!='n/a':
                count=int(row['count'])
            try:
                kcount=int(row['kcount'])
            except Exception:
                kcount=0

            spec,result=Specialty.objects.get_or_create(step=row['step'][0],name_of_specialty=row['title'],count_of_abiturients=count,
                                          count_of_contract_abiturients=kcount)
            subject=row['sub'].split(',')

            try:
                try:
                    coef=float(subject[1])
                    mark = int(subject[2])
                except ValueError:
                    coef=1
                    mark=100


                sub,res = Subject.objects.get_or_create(name_of_subject=subject[0],coef=coef,mark=mark)
            except IndexError:

                sub, res = Subject.objects.get_or_create(name_of_subject=subject[0], coef=float(subject[1]),

                                                         mark=100)

            if sub not in spec.subject_set.all():
                spec.subject_set.add(sub)

            if spec not in vnz[0].specialty_set.all():
                vnz[0].specialty_set.add(spec)
            students_name = row['students_name']
            priority = row['priority']
            mark=float(row['mark'])
            isdocument = row['isdocument']
            student,stres = Abiturient_Statement.objects.get_or_create(username=students_name,priority=priority,mark=mark,isdocument=isdocument)

            if student not in spec.students.all():
                spec.students.add(student)
            if student not in vnz[0].abiturient_statement_set.all():
                vnz[0].abiturient_statement_set.add(student)
    return HttpResponse("dndn")