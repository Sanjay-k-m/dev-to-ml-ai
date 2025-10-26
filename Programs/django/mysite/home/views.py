from django import template
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def homeCall(req):
    return render(req,'index.html')

def addform(req):
    return render(req,'addform.html')


def addVal(req):
    valone = int(req.POST['num1'])
    valtwo = int(req.POST['num2'])
    
    result = valone+valtwo
    
    return render(str,"result.html",{"result":result})