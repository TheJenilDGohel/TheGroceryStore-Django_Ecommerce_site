from multiprocessing import AuthenticationError
from telnetlib import AUTHENTICATION
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password , check_password
from django.contrib.auth.models import User,auth
from .models import Customer
from django.views import View

# Create your views here.


def logout(request):
    del request.session['User_id']
    del request.session['User_username']
    return redirect('login')


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['pass']
        retypepassword = request.POST['re_pass']
    
        if password ==retypepassword:
            if User.objects.filter(username=email).exists():
                messages.error(request,'Username Already Exists')
                return redirect('register')
            else:
                customer = Customer(first_name = first_name,last_name = last_name,password = password,email = email,username = email)
                customer.password = make_password(customer.password)
                customer.register() 
                user = User.objects.create_user(first_name = first_name,last_name = last_name,password = password,email = email,username = email)
                user.save()
                messages.info(request,"Registrated Successfully ! ")
                return redirect('login')

        else:
            messages.info(request,"Password Doesn't Match !!")
            return redirect('register')

    else:
        return render(request,"register.html")

class Login(View):
    def get(self,request):
        return render(request,"login.html")
    
    def post(self,request):
            email = request.POST['email']
            password = request.POST['pass']
            
            user = auth.authenticate(username = email,password = password)
            customer = Customer.get_customer_by_email(email)
            
            if user is None:
                messages.info(request,'Invalid Credentials')
                return redirect('login')

            else:
                auth.login(request,user)
                messages.info(request,'Login Succesfully')
                request.session['User_username'] = user.username
                request.session['User_id'] = user.id
            
            return redirect('home')