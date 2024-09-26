from django.shortcuts import render,redirect
from Product.models import Product
from django.contrib import messages

from django.http import HttpResponse
def product_list(request):
    all_products = Product.objects.all()
    data= {
        'Product': all_products,
        'title':"Daraz product page"
    }
    return render(request,"product.html",data)

def add_product(request):
    return render(request, 'add_product.html')

def ProductDetail(request,id):
    single_product =Product.objects.filter(id=id).first()
    data={
        'product':single_product,
    }
    return render(request,"single_product.html",data)


def store_product(request):
    if request.POST:
        product_name = request.POST['product_name']
        product_price = request.POST['product_price']
        product_category=request.POST['category']
        form_image=request.FILES['product_image']
        print(form_image)
        Product.objects.create(image=form_image,name=product_name,price=product_price,categories_id=product_category)
        messages.success(request, 'Product Added Successfully')
        return redirect('add_products')