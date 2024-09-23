from django.shortcuts import render
from Product.models import Product
def product(request):
    all_products = Product.objects.all()
    data= {
        'Product': all_products,
        'title':"Daraz product page"
    }
    return render(request,"product.html",data)
    
