# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UsersManager(models.Manager):
    def register(self, first_name, last_name, email, password, conf_password):
        message = []
        if len(first_name)<2 or len(last_name) <2:
            message.append('No fewer than 2 characters on name field')
        if not last_name.isalpha() or not first_name.isalpha():
            message.append('Only letters are allowed in name field')
        if len(email)<1:
            message.append('Email field required. Cannot be empty')
        if len(password)<1:
            message.append('Password Cannot be empty')
        if not EMAIL_REGEX.match (email):
            message.append('Please put valid email')
        if conf_password != password:
            message.append('Password do not match')
        if Users.usersManager.filter(email=email):
            message.append('Email already in database')
        if len(message)>0:
            return False, message
        else:
            user= Users.usersManager.create(first_name=first_name, last_name=last_name, email=email, password=password, conf_password=conf_password)
        return True, user


    def login(self, email, password):
        message = []
        if len(email)<1:
            message.append('Email field required. Cannot be empty')

        if len(password)<1:
            message.append('Password Cannot be empty')

        if len(message)>0:
            return False, message
        else:
            user=Users.usersManager.filter(email=email)
            if len(user)<1:
                message.append('Please register')
                return False, message
            elif password != user[0].password:
                message.append('Incorrect password')
                return False, message
            else:
                return True, user


class Users(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    conf_password= models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)
    usersManager= UsersManager()
