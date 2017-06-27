# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,reverse
from .models import User, Secret, Like
from django.contrib import messages
from django.db.models import Count

def index(request):
    return render (request, 'dojosecret_app/index.html')

def register(request):
    validate= User.userManager.register(request.POST["first_name"],request.POST["last_name"],request.POST["email"],request.POST["password"],request.POST["conf_password"])
    if validate[0] ==False:
        for errmsg in validate[1]:
            messages.add_message(request,messages.ERROR, errmsg)
        return redirect('/')
    else:
        request.session["loggedInUser"]= validate[1].first_name
        request.session["loggedInUserID"]= validate[1].id
        return redirect ('/secret')



def login(request):
    validate= User.userManager.login(request.POST["email"],request.POST["password"])
    if validate[0] == False:
        for errmsg in validate[1]:
            messages.add_message(request, messages.ERROR, errmsg)
        return redirect('/')
    else:
        request.session["loggedInUser"]= validate[1].first_name
        request.session["loggedInUserID"]= validate[1].id
        return redirect ('/secret')

def logout(request):
    request.session.clear()
    return redirect ('/')

def post(request):  #TO POST SECRET. ONCE IT'S DONE REDIRECTS BACK TO /SECRET PAGE
    Secret.secretManager.postsecret(request.POST["secret"], request.session["loggedInUserID"] )
    return redirect('/secret')

def secret(request):  #MAIN SECRET PAGE AFTER SUCCESSFUL LOGIN/REGISTRATION
    if not 'loggedInUser' in request.session:
        return redirect ('/')
    else:
        secrets=Secret.secretManager.all().annotate(num_likes=Count('liked_secret'))
        users=User.userManager.all()

        context= {
        "users": users,
        "secrets":secrets,
        }

        return render (request, 'DojoSecret_app/secret.html',context)


def secret_like(request, secretID):
    likes= Like.likeManager.likes(request.session["loggedInUserID"],secretID)
    if likes[0] == False:
        messages.add_message(request, messages.ERROR, likes[1])
        return redirect('/secret')
    else:
        print "You are liking this secret"
    return redirect('/secret')

def secret_delete(request, secretID):
    Secret.secretManager.filter(id=secretID).delete()
    return redirect('/secret')



def mostpopular(request):
    if not 'loggedInUser' in request.session:
        return redirect ('/')    
    else:
        users=User.userManager.all()
        secrets=Secret.secretManager.all().annotate(num_likes=Count('liked_secret')).order_by('-num_likes')[:5]
        context= {
        "users": users,
        "secrets":secrets,
        }

        return render(request, 'dojosecret_app/mostpopular.html', context)
