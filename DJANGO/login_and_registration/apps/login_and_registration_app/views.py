# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import UsersManager, Users
from django.contrib import messages


def index(request):
    return render(request, 'login_and_registration_app/index.html')


def register(request):
    validate= Users.usersManager.register(request.POST["first_name"],request.POST["last_name"],request.POST["email"],request.POST["password"],request.POST["conf_password"])
    all_users=Users.usersManager.all()
    if validate[0] ==False:
        for errmsg in validate[1]:
            messages.add_message(request,messages.ERROR, errmsg)
        return redirect('/')
    else:
        context ={
        "user_name": validate[1],
        "all_users": all_users
        }
        return render (request,'login_and_registration_app/success.html', context)



def login(request):
    validate= Users.usersManager.login(request.POST["email"],request.POST["password"])
    if validate[0] == False:
        for errmsg in validate[1]:
            messages.add_message(request, messages.ERROR, errmsg)
        return redirect('/')
    else:
        print validate[1]
        context= {
        "user_name": validate[1]
        }
    return render(request, 'login_and_registration_app/success.html',context)
