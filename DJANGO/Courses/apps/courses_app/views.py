# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Courses



def index(request):
    all_courses=Courses.objects.all()
    context= {
    "courses": all_courses
    }
    return render(request, 'courses_app/index.html',context)

def add(request):
    Courses.objects.create(course_name= request.POST['name'], description= request.POST['description'])
    return redirect ('/')

def deleteConf(request,id):
    course_to_remove= Courses.objects.filter(id=id)
    context ={
        "course_to_remove": course_to_remove
    }
    return render(request, 'courses_app/destroy.html',context)

def no(request):
    return redirect ('/')

def yes(request,id):
    Courses.objects.filter(id=id).delete()
    return redirect ('/')
