from django.http import HttpResponse
from django.shortcuts import render

def landingpage(request):
    data ={'title':"Daraz home page"}
    return render(request,"home.html",data)
    

def about(request):
    data ={'title':"Daraz About page"}
    return render(request,"about.html",data)
    

def categories(request):
    data ={'title':"Daraz categories page"}
    return render(request,"categories.html",data)
    

def contact(request):
    data ={'title':"Daraz contact page"}
    return render(request,"contact.html",data)
    



