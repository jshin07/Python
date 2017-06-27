# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'count' not in request.session:
        request.session['count']=1
    else:
        request.session['count'] +=1

    return render(request, 'first_app/index.html')

def generate(request):
    if request.method=="POST":
        ran_num= get_random_string(length= 32)
        print ran_num
        request.session['ran_num']=ran_num
    return redirect('/')
