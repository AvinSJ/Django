from django.shortcuts import render

# Create your views here.

from django.http import  HttpResponse
from django.template import loader
from .models import product

def productInfo(req):
    template=loader.get_template("productinfo.html")
    data= {"name": "VIVO",
           "desc": " Smart Phone",
           "price": 45555}
    return HttpResponse(template.render(data,req))



def productList(req):
    template=loader.get_template("productList.html")
    plist= product.objects.all()
    data= {

        "products":plist




    }
    return HttpResponse(template.render(data,req))