from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data ={'title':"Daraz home page"}
    return render(request,"home.html",data)
    




