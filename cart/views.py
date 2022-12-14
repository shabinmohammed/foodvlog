from django.shortcuts import render,redirect ,get_object_or_404
from shop.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def cart_details(request,tot=0,count=0,cart_items=None,ct_items=None):
    try:
        ct=Cartlist.objects.get(cart_id=c_id(request))
        ct_items=Items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot +=(i.prodt.price*i.quan)
            count += i.quan

        if tot < 1500:
            srs=40
            atot=tot+srs
        else:

            atot=tot
            srs = "free shipping"

    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',{'ci':ct_items,'t':tot,'cn':count,'at':atot,'sr':srs})

def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id



def add_cart(request,product_id):
    prod=Products.objects.get(id=product_id)
    try:
        ct=Cartlist.objects.get(cart_id=c_id(request))
    except Cartlist.DoesNotExist:
        ct=Cartlist.objects.create(cart_id=c_id(request))
        ct.save()

    try:
        c_items=Items.objects.get(prodt=prod,cart=ct)
        if c_items.quan < c_items.prodt.stock:
            c_items.quan+=1
        c_items.save()
    except Items.DoesNotExist:
        c_items=Items.objects.create(prodt=prod,quan=1,cart=ct)
        c_items.save()
    return  redirect('cartDetails')


def min_cart(request,product_id):
    ct=Cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(Products,id=product_id)
    c_items=Items.objects.get(prodt=prod,cart=ct)
    if c_items.quan>1:
        c_items.quan-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartDetails')

def cart_delete(request,product_id):
    ct = Cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(Products, id=product_id)
    c_items = Items.objects.get(prodt=prod, cart=ct)
    c_items.delete()
    return redirect('cartDetails')


