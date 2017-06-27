# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Users, UsersManager
from django.contrib import messages

def index(request):
    return render (request,'username_validation_app/index.html')

def user(request):
    if request.method== 'POST':
        validate_from_models= Users.usersManager.add_user(request.POST["username"])
        if validate_from_models[0]==False:
            message=validate_from_models[2][0]
            messages.error(request,message)
            return redirect ('/')
        else:
            user= validate_from_models[1]
            all_users= Users.usersManager.all()
            context={
            "user":user,
            "all_users":all_users
            }
            return render (request, 'username_validation_app/success.html',context)
