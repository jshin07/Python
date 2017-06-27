# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'first_app/index.html')

def projects(request):
    return render(request, 'first_app/projects.html')

def about(request):
    return render(request, 'first_app/about.html')

def testimonials(request):
    return render(request, 'first_app/testimonials.html')
    
# Create your views here.
