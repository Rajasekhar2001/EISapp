from django.shortcuts import render
from django.http import *
def signIn(request):
    return render(request,'index1.html')
def page1(request):
    email=request.POST.get('emailid')
    psswd=request.POST.get("password")
    if email=='krishnachaitanyajabu@gmail.com':
        if psswd=='1234567':
                return render(request,"display.html",{"e":email})
    elif email=='krishnachaitanyajabu@gmail.com':
        if psswd=='qwerty':
                return render(request,"display2.html",{"e":email})