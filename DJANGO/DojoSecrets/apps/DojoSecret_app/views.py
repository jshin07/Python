# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,reverse
from .models import UsersManager, Users, Secrets, SecretsManager, Likes
from django.contrib import messages
from django.db.models import Count

def index(request):
    return render (request, 'DojoSecret_app/index.html')



def register(request):
    validate= Users.usersManager.register(request.POST["first_name"],request.POST["last_name"],request.POST["email"],request.POST["password"],request.POST["conf_password"])
    if validate[0] ==False:
        for errmsg in validate[1]:
            messages.add_message(request,messages.ERROR, errmsg)
        return redirect('/')
    else:
        request.session["login_user"]= validate[1].first_name
        request.session["login_user_id"]= validate[1].id
        return redirect ('/secret')


def login(request):
    validate= Users.usersManager.login(request.POST["email"],request.POST["password"])
    if validate[0] == False:
        for errmsg in validate[1]:
            messages.add_message(request, messages.ERROR, errmsg)
        return redirect('/')
    else:
        request.session["login_user"]= validate[1].first_name
        request.session["login_user_id"]= validate[1].id
        return redirect ('/secret')

def logout(request):
    request.session.clear()
    return redirect ('/')

def secret(request):  #MAIN SECRET PAGE AFTER SUCCESSFUL LOGIN/REGISTRATION


    secrets=Secrets.secretsManager.all()
    likes=Likes.likesManager.all()


    context= {
    "user_name": request.session["login_user"],
    "secrets":secrets,
    "likes":likes,

    }
    return render (request, 'DojoSecret_app/secret.html',context)

def secret_like(request, secret_id):

    x= Secrets.secretsManager.get(id=secret_id)
    print x.like
    x.like +=1
    x.save()

    return redirect('/secret')




def post(request):  #TO POST SECRET. ONCE IT'S DONE REDIRECTS BACK TO /SECRET PAGE
    Secrets.secretsManager.postsecret(request.POST["secret"], request.session["login_user_id"] )
    return redirect('/secret')

def mostpopular(request): #WHEN MOSTPOPULAR LINK CLICEKD, IT REDIRECTS TO /show_mostpopular
    return redirect('/show_mostpopular')


def show_mostpopular(request):
    return render(request, 'DojoSecret_app/mostsecret.html')
