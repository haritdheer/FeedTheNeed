from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        
        contact.name=name
        contact.email=email
        contact.save()
        return HttpResponse("<h1>Thanks For Your Response.</h1>")

    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"Contact.html")