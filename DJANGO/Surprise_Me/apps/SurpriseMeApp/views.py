# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import random

VALUES = ['Chicken', 'Beer', 'Wine', 'Cheese', 'Party', 'Hangover','TGF', 'Crazy','Pizza', 'Merceredez']

def index(request):
    return render(request, 'SurpriseMeApp/index.html')

def results(request):
    if request.method =="POST":
        request.session['number']= request.POST['number']
        input_num= request.session['number']     ###input_num : input number the user passes
        ran_list =random.sample(VALUES,int(input_num))
        cleaned_list= u" , ".join(ran_list)

    context = {
    "surprises": cleaned_list,
    "input_num": input_num
    }
    return render(request, 'SurpriseMeApp/results.html',context)
