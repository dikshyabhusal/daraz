from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact
# Create your views here.
def contact(request):
    data ={'title':"Daraz contact page"}
    return render(request,"contact.html",data)
def store_contact(request):
    form_name=request.POST['text']
    form_email=request.POST['email']
    form_message=request.POST['message']

    #for database
    Contact.objects.create(name=form_name,email=form_email,message=form_message)
    messages.success(request,'Your message saved successfully.')
    return redirect('contacts')