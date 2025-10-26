from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.

def product(req):
    
    page = loader.get_template("homePage.html")
    data = {"name":"sanju"}
    response = page.render(data,req)
    return HttpResponse(response)