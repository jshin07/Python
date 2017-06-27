# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.shortcuts import render, HttpResponse


def index(request):
    context = {
    'current_time':datetime.datetime.now()
  }
    return render(request,'first_app/index.html', context)
# Create your views here.
