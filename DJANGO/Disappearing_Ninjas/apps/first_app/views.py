# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    return render(request,'first_app/index.html')

def ninjas(request):
    return render (request, 'first_app/ninjas.html')


def ninja(request,color):
    context= {
    "color":color
    }
    return render(request,'first_app/show.html', context)
