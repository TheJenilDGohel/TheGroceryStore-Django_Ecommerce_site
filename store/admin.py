from django.contrib import admin
from .models import Contact,Category,Product,order


class AdminCategory(admin.ModelAdmin):
    list_display =['name','description']

class AdminProduct(admin.ModelAdmin):
    list_display =['name','price','category']

class AdminOrders(admin.ModelAdmin):
    list_display =['customer_id','product','quantity','price','date']

admin.site.register(Category,AdminCategory)
admin.site.register(Product,AdminProduct)
admin.site.register(Contact)
admin.site.register(order,AdminOrders)

admin.site.site_header = "The Grocery Store"
