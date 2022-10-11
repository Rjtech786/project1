from concurrent.futures import process
from multiprocessing import context
from turtle import textinput
from unittest import result
from django.shortcuts import render,HttpResponse
from googletrans import Translator

def index(request):
    return HttpResponse("this is home page")

def traslate(request):
    result=""
    a=""
    if request.method=="POST":
        a=request.POST.get('text')
        b=request.POST.get('lang')
        translator = Translator()
        process = translator.translate(a, src='en', dest=b)
        result =process.text 
    else:
        pass
    return render (request,"translate.html" , {'text':a, 'output': result} )


