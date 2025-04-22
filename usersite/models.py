from unicodedata import category
from django.db import models


class User(models.Model):
    Name = models.CharField(max_length=250)
    Email = models.EmailField(unique = True)
    Age = models.IntegerField()
    Phone = models.CharField(max_length=50)
    Joined_At = models.DateTimeField(auto_now_add=True)
    Note = models.TextField()
    IsActive = models.BooleanField()
    Exact_Time = models.DateTimeField(auto_now_add=False)



def __str__(self):
    return self.Email 



class Category(models.Model):
    Category_Id = models.AutoField(primary_key=True)
    Category_Name = models.CharField(max_length=100, unique=True)
    Description = models.TextField(blank=True, null=True)
    Created_At = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.Catagory_Name
    


class Product(models.Model):
    Product_Id = models.AutoField(primary_key=True)
    Product_Name = models.CharField(max_length=100)
    Description = models.TextField(blank=True, null=True)
    Price = models.DecimalField(max_digit=10, decimal_places=2)
    Stock = models.IntegerField(default=0)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="Products", Created_at = models.DateTimeFieldauto_now_add=True) 


def __str__(self):
    return self.Product_Name                            



class Category(models.Model):
    Category_Id = models.AutoField(primary_key=True)
    Category_Name = models.CharField(blank=True, null=True)
    Description = models.TextField(blank=True, null=True)
    Created_At = models.DateTimeField(auto_new_add=True)


def __str__(self):
    return self.Category_Name



class Order(models.Model):
    Order_Id = models.Autofield(primary_key=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Orders')
    Order_Date = models.DateTimeField(auto_now_add=True)
    Total_Amount = models.DecimalField(max_digits=10, decimal_places=2)

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered')
        ('Cancelled', 'Cancelled'),
    ]
status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

def __str__(self):
    return f"Order {self.Order_Id} by User {self.user.User_Name}"



class Shopping_Cart(models.Model):
    Cart_Id = models.AutoField(primary_key=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Shopping_Carts')
    Created_At = models.DateTimeField(auto_now_add=True)



def __str__(self):
    return f"Cart {self.Cart_Id} for User {self.User.User_Name}"



class Payment(models.Model):
    Payment_Id = models.AutoField(primary_key=True)
    Order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='Payments')
    Payment_Date = models.DateTimeField(auto_now_add=True)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)


    PAYMENT_METHOD_CHOICES = [
        ('Credit Card', 'Credit Card')
        ('Paypal', 'Paypal')
        ('Bank Transfer', 'Bank Transfer'),
    ]
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered')
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')




def __str__(self):
    return f"Payment {self.Payment_Id} for Order {self.Order.Order_Id}"



class Shipping(models.Model):
    Shipping_Id = models.AutoField(primary_key=True)
    Order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='Shippings')
    Shipping_Address = models.CharField(max_length=255)
    Shipping_Date = models.DateTimeField(null=True, blank=True)
    Delivery_Date = models.DateTimeField(null=True, blank=True)

STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered')
        ('Cancelled', 'Cancelled'),
    ]
status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')



def __str__(self):
    return f"Shipping {self.Shipping_Id} for Order {self.Order.Order_Id}"

