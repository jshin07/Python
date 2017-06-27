# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Product

def index(request):
    Product.objects.create(name= "computer", description="the best one in the market", weight = 5, price = 1000, cost = 500, category= "electronics")
    Product.objects.create(name= "table", description="modern grey table", weight = 50, price = 500, cost = 350, category= "furnitures")

    products= Product.objects.all()
    print products
    context = {
        "products": products
    }
    return render (request, 'product_app/index.html',context)
