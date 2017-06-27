# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
    first_name= models.CharField(max_length = 255)
    last_name= models.CharField(max_length = 255)
    email= models.CharField(max_length = 255)
    password= models.CharField(max_length = 255)
    created_at= models.DateTimeField(auto_add_now= True)
    updated_at= models.DateTimeField(auto_add= True)

class Messages(models.Model):
    message= models.TextField()
    created_at= models.DateTimeField(auto_add_now= True)
    updated_at= models.DateTimeField(auto_add= True)
    user= models.ForeignKey(Users)

class Comments(models.Model):
    comments= models.TextField()
    created_at= models.DateTimeField(auto_add_now= True)
    updated_at= models.DateTimeField(auto_add= True)
    message= models.ForeignKey(Messages)
    user= models.ForeignKey(Users)
