from django.shortcuts import render

def product(request):
    data ={'title':"Daraz product page"}
    return render(request,"product.html",data)
    
