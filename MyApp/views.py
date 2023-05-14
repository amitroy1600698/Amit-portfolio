from django.http import HttpResponse
from django.shortcuts import render
from contactenquiry.models import contactenquiry

def homepage(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def gallery(request):
    return render(request,"gallery.html")
def saveEnquiry(request):
    if request.method == "POST":
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        message = request.POST.get('Message')
        en = contactenquiry(name=name, email=email,message=message)
        en.save()
    return render(request,"contact.html")