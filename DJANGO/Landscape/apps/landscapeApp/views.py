# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request,'landscapeApp/index.html')

def show(request, num):

    context = {
    "url": int(num)
    }
    print type(num)
    return render(request,'landscapeApp/show.html', context)
