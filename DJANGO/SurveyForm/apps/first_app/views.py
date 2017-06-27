# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render (request, 'first_app/index.html')

def result(request):
    if request.method=="POST":
        request.session['name']=request.POST["name"]
        request.session['location']=request.POST["location"]
        request.session['language']=request.POST["language"]
        request.session['comment']=request.POST["comment"]

# this doesn't work?!
    # if 'count' not in request.session:
    #     request.session['count']=1
    # else:
    #     request.session['count'] +=1

# this works
    if 'count' in request.session:
        request.session['count']+=1
    else:
        request.session['count']=1

        return redirect('/show')


def show(request):
    return render(request, 'first_app/result.html')
