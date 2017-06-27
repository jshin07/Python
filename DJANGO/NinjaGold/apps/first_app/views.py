# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect,
import random
from datetime import datetime

def index(request):
    if 'count' not in request.session:
        request.session['count']=0
    if 'message' not in request.session:
        request.session['message']=[]
    return render(request, 'first_app/index.html')

def process_money(request):
    if request.method== "POST":
        if request.POST['building'] == "farm":
            farmCount = random.randint(10,20)
            request.session['count'] += farmCount
            msg = "Earned "+ str(farmCount)+ " golds from the farm!"
            # print msg

        elif request.POST['building'] == "cave":
            caveCount = random.randint(5,11)
            request.session['count'] += caveCount
            msg = "Earned "+ str(caveCount)+ " golds from the cave!"

        elif request.POST['building'] == "house":
            houseCount = random.randint(2,5)
            request.session['count'] += houseCount
            msg = "Earned "+ str(houseCount)+ " golds from the house!"

        elif request.POST['building'] == "casino":
            casinoCount = random.randint(-50,50)
            if casinoCount >0:
                request.session['count'] += casinoCount
                msg = "Earned "+ str(casinoCount)+ " golds from the casino!"
                # print msg
            else:
                request.session['count'] += casinoCount
                msg = "Lost "+ str(casinoCount)+ " golds from the casino! Ouch!"
                # print msg

        request.session['message'] += msg  + "\n"

        return redirect('/')
