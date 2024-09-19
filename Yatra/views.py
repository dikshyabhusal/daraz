from django.http import HttpResponse
from django.shortcuts import render

def landingpage(request):
    return render(request,"home.html")
    return HttpResponse(html)

def about(request):
    return render(request,"about.html")
    return HttpResponse(html)

def product(request):
    return render(request,"product.html")
    return HttpResponse(html)

def categories(request):
    return render(request,"categories.html")
    return HttpResponse(html)

def contact(request):
    return render(request,"contact.html")
    return HttpResponse(html)



