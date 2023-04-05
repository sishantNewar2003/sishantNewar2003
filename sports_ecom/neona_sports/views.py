from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product, Contact_us, Main_category, Category
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib import messages



# Create your views here.
@login_required(login_url='login')
 
def base(request):
    return render(request, 'base.html')


def hi(request):
    return render(request,'home.html')


def loginpage(request):
    if request.method=="POST":
        user_name=request.POST.get('username')
        pass1=request.POST.get('pass')
        
        
        user=authenticate(request, username=user_name, password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request, "you have logged in successfully")
            return redirect('home')
            
        else:
            messages.error(request, "Your Username or Password is incorrect")
          
           

    return render(request,'login.html')
 

def signup(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            messages.error(request, "Your Password didn't match") 
            return redirect('signup')
        else:
           my_user=User.objects.create_user(uname,email,pass1)
           my_user.save()
           messages.success(request, "Your account has been created")
           return redirect('loginpage')

        
        

    return render(request,'signup.html')    

 
def logoutpage(request):
    logout(request)
    return redirect('loginpage')


def  product(request):

    main_category = Main_category.objects.all().order_by('-id')
    product = Product.objects.filter()
    category = Category.objects.all().order_by('-id')

    categoriesID = request.GET.get('categories')

    if categoriesID:
        product = Product.objects.filter(category = categoriesID)
    else:
        product = Product.objects.filter()
   
    data = {
        'main_category' : main_category,
        'product': product,
        'category': category,
    
    }

    return render(request, 'product.html', data)

def product_detail(request,id):
    product = Product.objects.filter(id = id).first()
    context = {
        'product':product
    }
    return render(request, 'product_detail.html', context)    
    



def Contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        # phone_number = request.POST.get('phone_number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        

        contact = Contact_us(
            name=name,
            email=email,
            # phone_number=phone_number,
            subject=subject,
            message=message,

        )

        contact.save()
        return redirect('home')


    return render(request, "contact.html")



def profile(request):
    # check if the user is authenticated or not
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect("loginpage")




@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)

    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')

