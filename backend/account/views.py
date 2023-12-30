from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def user_register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if User.objects.filter(email = email).exists():
            messages.error(request, "User wuth this email id already registered")
            return redirect('/register')
        else:
            if password1 != password2:
                messages.error(request, "passwords does not match")
                return redirect('/register')
            else:
                new_user = User.objects.create_user(
                    first_name = first_name,
                    last_name = last_name,
                    email=email,
                    username = email
                )
                new_user.set_password(password1)
                new_user.save()
                return redirect('/login')

    return render(request, "files/register.html")

def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not User.objects.filter(email = email).exists():
            messages.error(request, "The user with this email id is not registered")
            return redirect("/login")
        user = authenticate(username = email, password=password)
        if user is None:
            messages.error(request, "Invalid Password")      
            return redirect("/login")      
        else:
            login(request, user)
            return redirect('/home')
        
    return render(request, "files/login.html")

def user_logout(request):
    logout(request)
    return redirect("/login")


def update_account(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        # if request.user.email != User.objects.get(email = email) and User.objects.filter(email = email).exists():
        #     messages.error(request, "User with this email id exists")
        #     return redirect("/account")

        user = User.objects.get(email = email)
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return redirect("/home")
    return render(request, "files/update.html", context= {"user" : request.user})