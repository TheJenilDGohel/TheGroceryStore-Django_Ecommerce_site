from django.db import models

# Create your models here.

class Customer(models.Model):
    username = models.CharField(max_length=255)
    first_name =  models.CharField(max_length=255)
    last_name =  models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=500)  

    def register(self):
        self.save()
    
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False

    def __str__(self):
        return self.username
    