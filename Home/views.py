from django.shortcuts import render
from Home.models import Home
from Product.models import Product
def home(request):
    all_home = Home.objects.all()
    products =  Product.objects.all()
    data= {
        'Home': all_home,
        'title':"Daraz Home page",
        'products': products,
    }
    return render(request,"home.html",data)
