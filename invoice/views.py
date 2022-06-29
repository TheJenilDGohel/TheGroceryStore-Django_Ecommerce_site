from django.shortcuts import render
from store.models import order,Product
from accounts.models import Customer
import uuid
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa 
from django.conf import settings

# Create your views here.

def show_invoice(request):
    if request.method == 'GET':
        current_user = request.session.get('User_id')
        order_cust = order.objects.filter(customer_id = current_user)
        
        x = uuid.uuid1()

        invoice_no = "Invoice No : " + str(x)[:7]

        context = {}
        context['order_cust'] = order_cust
        context['current_user'] = current_user
        context['invoice_no'] = invoice_no

        return render(request, "invoice.html", context)


