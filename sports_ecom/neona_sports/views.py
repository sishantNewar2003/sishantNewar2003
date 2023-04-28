import os

from cart.cart import Cart
from django.contrib import messages
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template import RequestContext
import requests


from .models import (Category, Contact_us, Customer, Main_category, Order,
                     Product)

# Create your views here.

def base(request):
    return render(request, 'base.html')


def hi(request):
    data = Product.objects.filter(featured=True).order_by('-id')

    return render(request,'home.html', {'data':data})


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
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if User.objects.filter(username=username):
            messages.error(request, "username already exist!!")
            return redirect('signup')
        
        if User.objects.filter(email=email):
            messages.error(request, "email already exist!")
            return redirect('signup')        
        
        if pass1!=pass2:
            messages.error(request, "Your Password didn't match") 
            return redirect('signup')
        else:
           my_user=User.objects.create_user(username,email,pass1)
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
        product = Product.objects.all()
   
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
    


@login_required(login_url="/loginpage/")
def Contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        messages.success(request, "your contact has been send")

        contact = Contact_us(
            name=name,
            email=email,
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

def Aboutus(request):
    return render(request, 'aboutus.html')


@login_required(login_url="/users/loginpage/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/loginpage")
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

def Checkout(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        
        
        messages.success(request, "your order has been placed")

        order = Order(
            firstname=firstname,
            lastname=lastname,
            email=email,
            address=address,
            mobile=mobile,

        )

        order.save()
        return redirect('khalti')
    
    return render(request, 'checkout.html')

def admin(request):
    contact = Contact_us.objects.filter()

    data = {
        
        'contact': contact,
    
    }
    return render(request, 'admin/adminpanel.html', data)

def ADD(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact_us(
            name=name,
            email=email,
            subject=subject,
            message=message,

        )
        contact.save()

        return redirect('admin')
    
    return render(request, 'admin/adminpanel.html')


def Edit(request):
    contact = Contact_us.objects.filter()
    

    context = {
        'contact':contact,
    }
    return redirect(request, 'admin/adminpanel.html', context)


def Update(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
    

        contact = Contact_us(
            id = id,
            name = name,
            email = email,
            subject = subject,
            message = message,

        )
        contact.save()

        return redirect('admin')
         
 
    return redirect(request, 'admin/adminpanel.html')

def Delete(request, id):
    contact = Contact_us.objects.filter(id=id)
    contact.delete()

    context = {
        'contact':contact
    }

    return redirect('admin', context)

def Changepass(request):
    if request.method == "POST":
      passchange = PasswordChangeForm(user=request.user, data=request.POST)
      if passchange.is_valid():
        passchange.save()
        update_session_auth_hash(request, passchange.user)
        return HttpResponseRedirect('/profile/')
    else:
        passchange = PasswordChangeForm(user=request.user)
    return render(request, 'changepassword.html', {'form':passchange})


def prodadmin(request):
    product = Product.objects.filter()

    data = {
        
        'product': product,
    
    }
    return render(request, 'admin/productadmin.html', data)


def dashboard(request):
    order=Order.objects.all()
    customer=Customer.objects.all()
    total_customer=customer.count()
    total_order=order.count()
    

    context={
        'order':order,
        'customer':customer,
        'total_customer':total_customer,
        'total_order':total_order,
        
    }

    return render(request, 'admin/adimindashboard.html', context)

def adminlogin(request):
   
     if request.method=="POST":
        user_name=request.POST.get('username')
        pass1=request.POST.get('pass')
        
        
        user=authenticate(request, username=user_name, password=pass1)
        if user is not None and user.is_staff:
            login(request,user)
            messages.success(request, "you have logged in successfully")
            return redirect('dashboard')
            
        else:
            messages.error(request, "Your Username or Password is incorrect")
          
     return render(request, 'admin/adminlogin.html')




def addProduct(request):
    if request.method == "POST":
        prod = Product()
        prod.name = request.POST.get('name')
        prod.price = request.POST.get('price')
        prod.categories = request.POST.get('categories')

        if len(request.FILES) != 0:
            prod.image = request.FILES['image']

        prod.save()
        messages.success(request,"Product succesfully added")
        return redirect('prodadmin')    

    return render(request, 'admin/addproduct.html')


def editProduct(request, st):
    prod = Product.objects.get(id=st)

    if request.method == "POST":
        if len(request.FILES) !=0:
            if len(prod.image) > 0:
                os.remove(prod.image.path)
            prod.image = request.FILES['image']
        prod.name = request.POST.get('name')
        prod.price = request.POST.get('price')
        prod.categories = request.POST.get('categories')

        prod.save()

        messages.success(request, "Product Updated successfully")
        return redirect('prodadmin')
    
    context ={
        'prod':prod
    }
    return render(request, 'admin/editproduct.html', context)

def deleteProduct(request, st):
    prod = Product.objects.filter(id=st)
    prod.delete()
    messages.success(request,"product deleted sucessfully")
    return redirect('prodadmin')

def khalti(request):

   
    context={
    
    }
    return render(request, 'khalti.html', context)

def khalti_verify(request):
   token = request.GET.get("token")
   amount = request.GET.get("amount") 
   print(token, amount)
    
   url = "https://khalti.com/api/v2/payment/verify/"

   payload = {
        'token': token,
        'amount': amount,
    }

   headers = {
        'Authorization': 'Key test_secret_key_f73da06a8242411686e3e37a65103412'
    }
   
   response = requests.request("POST", url, headers=headers, data=payload)
   resp_dict = response.json()
   if resp_dict.get("idx"):
       success = True
     

   else:
       success = False


   data={
      "success": success
   }
   return JsonResponse(data)

def Wishlist(request,id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('wishlist')


