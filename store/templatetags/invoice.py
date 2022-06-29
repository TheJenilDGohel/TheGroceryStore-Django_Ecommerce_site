from django import template

register = template.Library()

@register.filter(name='totalamount')
def totalamount(order_cust):
    price = order_cust.price
    product_quantity = order_cust.quantity

    return price * product_quantity


@register.filter(name='total_cust_price')
def total_cust_price(order_cust):
    sum = 0;
    for p in order_cust:
        sum+=totalamount(p)
    
    return sum

@register.filter(name='userphone')
def userphone(order_cast):
    for order_cast in order_cast:
        phone = order_cast.phone 
    
    return phone

@register.filter(name='useremail')
def useremail(order_cast):
    for order_cast in order_cast:
        email = order_cast.customer_id 
    
    return email

@register.filter(name='useraddress')
def useraddress(order_cast):
    for order_cast in order_cast:
        address = order_cast.address 
    
    return address