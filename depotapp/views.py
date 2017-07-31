from django.shortcuts import render
from django.http import request,HttpResponse
from depotapp.models import Product
from django.template import loader,Context,RequestContext
from django import forms
# -*- coding:utf-8 -*-



# Create your views here.

def product_list(request):
    product_list=Product.objects.all()
    t=loader.get_template('product_list.html')
    html=t.render(Context({"product_list":product_list}))
    return HttpResponse(html)

def create_product(request,id):
    return '1'

def view_product(request,id):
    assert False
    product_instance=Product.objects.get(id=id)
    t=loader.get_template('view_product.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_product(request,id):
    return '1'