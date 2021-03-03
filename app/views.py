"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
# -*- coding: utf-8 -*-
from app.models import Contact
import pyodbc
import sys
sys.setrecursionlimit(16385)
from django.contrib import messages
  




def index(request):
    # return HttpResponse("This is homepage")
    return render(request,'app/index.html')

def about(request):
    return render(request,'app/about.html')

def services(request):
    return render(request,'app/services.html')

def loginpage(request):
    return render(request,'app/loginpage.html')

def contact(request):
    if request.method == "POST":
         name = request.POST.get('name')
         email = request.POST.get('email')
         query = request.POST.get('query')
         contact = Contact(name=name, email=email, query=query)
         contact.save()
         messages.success(request, 'Your details have been saved')

    return render(request,'app/contact.html')