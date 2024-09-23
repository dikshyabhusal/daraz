from django.shortcuts import render
from About.models import About 
# Create your views here.
def about(request):
    all_abou=About.objects.all()
    data={
        'About':all_abou
    }
    return render(request,'About.html',data)