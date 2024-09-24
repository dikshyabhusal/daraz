from django.shortcuts import render
from Product.models import Product
def product_list(request):
    all_products = Product.objects.all()
    data= {
        'Product': all_products,
        'title':"Daraz product page"
    }
    return render(request,"product.html",data)

def ProductDetail(request,id):
    single_product =Product.objects.filter(id=id).first()
    data={
        'product':single_product,
    }
    return render(request,"single_product.html",data)
