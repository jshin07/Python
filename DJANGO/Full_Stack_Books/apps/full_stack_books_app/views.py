# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Books

def index(request):
    books=Books.objects.all()
    context = {
    "books":books
    }
    return render(request, 'full_stack_books_app/index.html',context)

def books(request):
    Books.objects.create(title=request.POST['title'], category=request.POST['category'], author= request.POST['author'])

    return redirect ('/')
