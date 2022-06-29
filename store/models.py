from django.db import models
from django.conf import settings
import datetime

#product-category details Model
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=70)
    image = models.ImageField(upload_to = 'Images/catgeories/')

    def __str__ (self):
        return self.name

    @staticmethod
    def get_all_category():
        return Category.objects.all()

#product-category details Model
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=200,default='')
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to = 'Images/products/',default ='')


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(product_id__in = ids)
        
    def __str__ (self):
        return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_product_id(product):
        return product.product_id

    @staticmethod
    def get_product_count(products):
        count = 0
        for product in products:
            count +=1
        
        return count
    
    @staticmethod
    def get_all_products_by_id(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        
        else:
            return Product.get_all_products();

# Contact Page Model
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField()
    timestamp = models.DateTimeField()  

    def __str__(self):
        return self.name

# Cart Model
class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE,default = 1)
    quantity = models.IntegerField(default = 1)
    price = models.IntegerField()
    address = models.CharField(max_length=150, default = '', blank =True)
    phone = models.CharField(max_length = 13 , default = '', blank = True)
    date = models.DateField(default =datetime.datetime.today)
    status_choices = (('Received', 'Received'),
        ('Scheduled', 'Scheduled'), 
        ('Shipped','Shipped'),
        ('Delivered','Delivered'),
        )
    status = models.CharField(max_length = 100, choices = status_choices, default="In Progress")
    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer):
       return order.objects.filter(customer_id = customer)
