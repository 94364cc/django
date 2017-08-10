from django.shortcuts import render,get_object_or_404
from django.http import request,HttpResponse
from depotapp.models import Product
from django.template import loader,Context,RequestContext
from django.shortcuts import render_to_response
from forms import *
# -*- coding:utf-8 -*-

def product_list(request):
    product_list=Product.objects.all()
    t=loader.get_template('product_list.html')
    html=t.render(Context({"product_list":product_list}))
    return HttpResponse(html)

def create_product(request):
    form=ProductForm(request.POST or None)

    if form.is_valid:
        form=ProductForm
    return render_to_response('create_product.html',locals())

def add_product(request):
    title=request.POST['title']
    description=request.POST['description']
    price=request.POST['price']
    image_url=request.POST['image_url']
    Product.objects.create(title=title,description=description,price=price,image_url=image_url)

    product_list=Product.objects.all()
    return render_to_response('product_list.html',{'product_list':product_list})

def view_product(request,id):
    product_instance=Product.objects.get(id=id)
    t=loader.get_template('view_product.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_product(request,id):
    product=Product.objects.get(id=id)

    form=ProductForm(request.POST or None, instance = product)
    if form.is_valid():
        form.save()
    return render_to_response('edit_product.html',locals())

def update_product(request):
    if request.method=="POST":
        product_id=request.POST['id']
        title=request.POST['title']
        description=request.POST['description']
        price=request.POST['price']

        Product.objects.filter(title=title).update(description=description,price=price)

    product_list=Product.objects.all()
    return render_to_response('product_list.html',{'product_list':product_list})

def delete_product(request,id):
    product=get_object_or_404(Product,pk=id)
    product.delete()
    product_list=Product.objects.all()
    return render_to_response('product_list.html',{'product_list':product_list})