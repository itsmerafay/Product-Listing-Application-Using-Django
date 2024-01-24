from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

# login maintains session in the browser

# Create your views here.
@login_required
def index(request):
    
    data =  request.POST
    if request.method == "POST":
        product_name = data.get("product_name")
        product_description = data.get("product_description")
        product_image = request.FILES.get("product_image")


        Product.objects.create(
            product_name = product_name,
            product_description = product_description,
            product_image = product_image,
            user = request.user
        )
        # for the purpose of refresh

        return redirect('/index/')     


    return render(request, "index.html")

@login_required
def table(request):
    if request.method == "GET":
        queryset = Product.objects.filter(user=request.user)
            
        if request.GET.get("search"):
            queryset = queryset.filter(product_name__icontains = request.GET.get("search"))
        context = {'products':queryset}
                

    return render(request, "table.html", context)

@login_required
def deleteproduct(request, id):
    queryset = Product.objects.get(id=id)
    queryset.delete() 

    return redirect('/table/')

@login_required
def updateproduct(request, id):
    queryset = Product.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        product_name = data.get("product_name")
        product_description = data.get("product_description")
        product_image = request.FILES.get("product_image")

        # Check if a file is provided before updating the field
        if product_image:
            queryset.product_image = product_image

        # Update other fields
        queryset.product_name = product_name
        queryset.product_description = product_description
        queryset.save()

        return redirect("/table/")

    context = {"product": queryset}
    return render(request, "update_product.html", context)



def login_page(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")

        print("Username:", username)
        print("Password:", password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check if the user exists before accessing the password
            if not user.password:
                messages.error(request, "Invalid Password")
                return redirect('/login/')
            
            login(request, user)
            return redirect('/index/')
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect('/login/')

    return render(request, "login.html")




def register_page(request):

    if request.method == "POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        password = data.get("password")


        user_exists = User.objects.filter(username=username).exists()
        if user_exists:
            messages.info(request, "Username already exists !! ")
            return redirect('/register/')


        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )

        # built-in object for setting password in hash format

        user.set_password(password)
        user.save()
        
        messages.info(request, "Account created successfully !! ")

        return redirect('/login')

    return render(request, "register.html")



def logout_page(request):   
    logout(request)
    return redirect('/login/')
