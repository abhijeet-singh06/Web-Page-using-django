from django.shortcuts import render,HttpResponse

from Shop.models import Contact

# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def home(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        
        c = Contact(name=name,email=email,phone=phone,message=message)
        c.save()  
        
    data = Contact.objects.all()   
    return render(request,"contact.html",{"data":data})

