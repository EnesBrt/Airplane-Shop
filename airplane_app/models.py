from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    id_client = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = PhoneNumberField(unique=True)


class Orders(models.Model):
    id_order = models.BigAutoField(primary_key=True)
    id_client = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    date_order = models.DateTimeField(auto_now=True)
    status_order = models.CharField()
    id_transaction = models.CharField() #?


class Products(models.Model):
    id_product = models.BigAutoField("Product Id", primary_key=True)
    name = models.CharField("Product name", null=False)
    description = models.TextField("Product description", null=False)
    price = models.FloatField("Product price", null=False)
    image = models.ImageField("Product image", null=False)
    stock = models.IntegerField("Product remaining stock", null=False)


class OrderDetails(models.Model):
    id_order = models.ForeignKey("Order Id", to=Orders, on_delete=models.CASCADE)
    id_product = models.ForeignKey("Product Id", to=Products, on_delete=models.CASCADE)
    quantity = models.IntegerField("Quantity of ordered product", null=False)
    price = models.FloatField("Total price of the order", null=False)
