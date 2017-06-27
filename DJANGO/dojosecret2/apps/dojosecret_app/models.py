# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import re
import bcrypt


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
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
            message.append('Please put a valid email')
        if conf_password != password:
            message.append('Password do not match')
        if User.userManager.filter(email=email):
            message.append('Email already in database')
        if len(message)>0:
            return False, message
        else:
            hashed= bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            user= User.userManager.create(first_name=first_name, last_name=last_name, email=email, password=hashed)
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
            user=User.userManager.filter(email=email)
            if len(user)<1:
                message.append('Please register')
                return False, message
            if not bcrypt.checkpw(password.encode('utf-8'),user[0].password.encode('utf-8')):
                message.append('Incorrect password')
                return False, message
            else:
                return True, user[0]



class SecretManager(models.Manager):
    def postsecret(self, secretmsg, user):
        data= Secret.secretManager.create(secretmsg= secretmsg, user_id=user)  # uers_id comes from the Secrets table it's actually user, but have to add _id. user comes from the parameter that came from the Users.secretsManager.postsecret


        return True, data

class LikeManager(models.Manager):
    def likes(self, user, secret):
        x= Like.likeManager.filter(user_id=user,secret_id=secret)
        if len(x)>0:
            return (False, "You already liked that secret")
        else:
            liked= Like.likeManager.create(user_id=user, secret_id=secret)
            return (True, liked)

    def ifLiked(self, user, secret):
        message = []
        x= Like.likeManager.filter(user_id=user,secret_id=secret)
        if len(x)>0:
            message.append("You already liked this")
            return message



class User(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)
    userManager= UserManager()


class Secret(models.Model):
    secretmsg= models.TextField()
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)
    secretManager=SecretManager()
    user=models.ForeignKey(User)


class Like(models.Model):
    user= models.ForeignKey(User, related_name= "liked_user")
    secret=models.ForeignKey(Secret, related_name= "liked_secret")
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)
    likeManager=LikeManager()
