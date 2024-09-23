from django.shortcuts import render
from Home.models import Home 
def home(request):
    all_home = Home.objects.all()
    data= {
        'Home': all_home,
        'title':"Daraz Home page",
    }
    return render(request,"home.html",data)
