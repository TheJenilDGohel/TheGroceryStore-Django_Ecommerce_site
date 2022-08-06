from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
from .models import Contact, Product, Category, order
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Class Based View
class Home(View):
    # @login_required
    def post(self, request):
        product_id = request.POST.get('product_id')
        product_qty = request.POST.get('p_qty')
        cart = request.session.get('cart')
        customer = request.session.get('User_username')

        if customer:
            if cart:
                quantity = cart.get(product_id)

                if quantity:
                    cart[product_id] += int(product_qty)

                else:
                    cart[product_id] = int(product_qty)
            else:
                cart = {}
                cart[product_id] = int(product_qty)

            print(cart)
            request.session['cart'] = cart
            return redirect('home')
        else:
            messages.info(request, 'You need to login  First')
            return redirect('login')

        wishlist = request.session.get('wishlist')
        if customer:
            if wishlist:
                quantity = wishlist.get(product_id)

                if quantity:
                    wishlist[product_id] += int(product_qty)

                else:
                    wishlist[product_id] = int(product_qty)

            else:
                wishlist = {}
                wishlist[product_id] = int(product_qty)

            request.session['wishlist'] = wishlist
            print(request.session['wishlist'])
            return redirect('home')

        else:
            messages.info(request, 'You need to login  First')
            return redirect('login')

    def get(self, request):
        products = None
        categories = Category.get_all_category()
        category_id = request.GET.get('category')
        data = {}
        data['categories'] = categories
        data['products'] = products

        if category_id:
            products = Product.get_all_products_by_id(category_id)
            data['products'] = products
            return render(request, 'category.html', data)

        else:
            products = Product.get_all_products()
            data['products'] = products

         # print('you are : ',request.session.get('User_username'))
         #print('your id : ',request.session.get('User_id'))

        return render(request, "home.html", data)

# Create your views here.


def about(request):
    return render(request, "about.html")


class shop(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        product_qty = request.POST.get('p_qty')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product_id)

            if quantity:
                cart[product_id] += int(product_qty)

            else:
                cart[product_id] = int(product_qty)
        else:
            cart = {}
            cart[product_id] = int(product_qty)

        print(cart)
        request.session['cart'] = cart
        return redirect('shop')

    def get(self, request):
        products = None
        productcount = 0
        categories = Category.get_all_category()
        category_id = request.GET.get('category')
        data = {}
        data['categories'] = categories
        data['products'] = products
        data['productcount'] = productcount

        if category_id:
            products = Product.get_all_products_by_id(category_id)
            data['products'] = products
            return render(request, 'category.html', data)

        else:
            products = Product.get_all_products()
            productcount = Product.get_product_count(products)
            data['products'] = products
            data['productcount'] = productcount

         # print('you are : ',request.session.get('User_username'))
         #print('your id : ',request.session.get('User_id'))

        return render(request, "shop.html", data)

# contact page sending to postgres


def contact(request):
    if request.method == 'POST':
        Name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['number']
        message = request.POST['msg']

        current_datetime = datetime.now()

        data = Contact(name=Name, email=email, phone=phone,
                       message=message, timestamp=current_datetime)
        data.save()

        messages.info(request, "Feedback Posted")
        return redirect('contact')

    else:
        return render(request, 'contact.html')


class Cart(View):
    def post(self, request):
        pass

    def get(self, request):
        id_list = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(id_list)

        return render(request, "cart.html", {'products': products})


class Wishlist(View):
    def post(self, request):
        pass

    def get(self, request):
        id_list = list[request.session.get('wishlist').keys()]
        print(id_list)
        products = Product.get_products_by_id(id_list)

        return render(request, "wishlist.html", {'products': products})


def category(request):
    if request == 'POST':
        pass

    else:
        products = None
        categories = Category.get_all_category()
        category_id = request.GET.get('category')

        if category_id:
            products = Product.get_all_products_by_id(category_id)

         # print('you are : ',request.session.get('User_username'))
         #print('your id : ',request.session.get('User_id'))
        data = {}
        data['categories'] = categories
        data['products'] = products
        return render(request, "category.html", data)


def clear_cart(request):
    request.session['cart'] = {}
    return redirect('home')


# MV Review
def review(request):
    return render(request, "review.html")

# User Profile


def user_profile(request):
    if request.method == 'POST':
        return render(request, "user_profile_update.html")
    else:
        return render(request, "user_profile_update.html")

# Check-Out Page


def checkout(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('number')
        address = request.POST.get('address')
        email = request.POST.get('email')
        payment_method = request.POST.get('method')
        cart = request.session.get('cart')
        customer = request.session.get('User_username')

        products = Product.get_products_by_id(list(cart.keys()))

        for product in products:
            product_id = product.get_product_id(product)
            Order = order(customer_id=User.objects.get(username=customer),
                          product=product,
                          price=product.price,
                          quantity=cart.get(str(product_id)),
                          address=address,
                          phone=phone)
            print(Order)
            Order.placeOrder()

        request.session['cart'] = {}

        return redirect('invoice')

    else:
        return render(request, "checkout.html")

# Orders Page


class Orders(View):
    def get(self, request):
        customer = request.session.get('User_id')
        orders = order.get_orders_by_customer(customer)

        return render(request, 'orders.html', {'orders': orders})

# Search Product


class Search(View):
    def get(self, request):
        return render(request, 'search_page.html')

    def post(self, request):
        query_name = request.POST.get('search')
        products = []
        if query_name:
            products = Product.objects.filter(
                name__icontains=query_name).order_by('-product_id')
            return render(request, 'search_page.html', {"products": products})

        else:
            return render(request, 'search_page.html', {"products": products})
