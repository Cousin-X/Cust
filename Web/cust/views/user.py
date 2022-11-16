from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        print(request.POST)
       #添加session request.session['user'] = {'job':"",'name':"",' identit':""}
        return HttpResponse("200")

def reg(request):
    return render(request,"reg.html")


def admin(request):
    return render(request,"admin.html")