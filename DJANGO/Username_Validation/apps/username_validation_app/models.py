# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UsersManager(models.Manager):
    def add_user(self,username):
        message=[]
        if len(username)<8:
            message.append("Your user name cannot be less than 8 characters")
            # print message
            validate= (False, username, message)
            return validate
        elif len(username)>26:
            message.append("Your user name cannot exceed 26 characters")
            # print message
            validate= (False, username, message)
            return validate
        else:
            message.append("You entered a valid user name")
            # print message
            validate= (True, username, message)
            all_users= Users.usersManager.create(username=username)
            print all_users
            return validate



class Users(models.Model):
    username=models.CharField(max_length=26)
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)
    usersManager= UsersManager()
