from django.shortcuts import render,redirect
from .models import user
def index(request):
    users={
        "all_users":
        user.objects.all()
    }
    print (users)
    return render(request,'index.html',users)

def add(request):
    return render(request,'add_user.html')

def user_to_add(request):
    user.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email_address=request.POST['email'],age=request.POST['age'])
    return redirect("/add_user")
    