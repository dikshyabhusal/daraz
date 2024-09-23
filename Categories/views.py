from django.shortcuts import render
from Categories.models import Categories
# Create your views here.
def categories(request):
    all_cate = Categories.objects.all()
    data ={
        'Categories':all_cate
    }
    return render(request,'Categories.html',data)
