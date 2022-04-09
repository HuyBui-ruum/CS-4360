from django.db import models
from django.utils.translation import gettext as _
from datetime import datetime, timedelta
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    """ Book model with ISBN, title, authors, year public, price, quantity and thumbnail"""
    isbn = models.CharField(_("isbn"), max_length = 30, primary_key = True)
    title = models.CharField(_("title"), max_length = 100)
    authors = models.CharField(_("authors"), max_length = 100)
    year_public = models.IntegerField(_("year_public"), null = True)
    publisher = models.CharField(_("publisher"), max_length = 100, null = True)  
    thumbnail_pic = models.ImageField(_("thumbnail_pic"), null = True, blank = True, upload_to ="static/images/books")
    price = models.IntegerField(_("price"))
    quantity = models.IntegerField(_("Quantity"))

    def __str__(self):
        """String for representing the Book title."""
        return self.title

    def decrease_quantity(self, quantity_to_decrease):
        print("Current Quantity: " + str(self.quantity) + " Amount to Decrease: " + str(quantity_to_decrease))
        if (quantity_to_decrease < self.quantity):
            self.quantity = self.quantity - quantity_to_decrease
            self.save()
            print("New Quantity: " + str(self.quantity))
        
# Customer Model
class Customer(models.Model):
    """A customer model to store basic identifying information for customer end users."""

    # Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    address_1 = models.CharField(_("address"), max_length = 128)
    city = models.CharField(max_length = 128)
    state = models.CharField(max_length = 128)
    zip_code = models.CharField(max_length = 5)
    
    def __str__(self):
        """String for representing the Book title."""
        return self.last_name

class Order(models.Model):
    """ Cart/Order model """
    customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, blank=True, null=True) #ForeignKey => so one to many relationship which one customer can have many orders
    date_order = models.DateTimeField(auto_now_add=True) #When order created
    complete = models.BooleanField(default=False, null=True, blank=False) # if complete is false then customer can continue to adding items to that cart
    transaction_id = models.CharField(max_length=200, null=True) # add some extra info to order
    
    def __str__(self):
        return str(self.id)
    @property
    # get total price for cart
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        rentitems = self.rentitem_set.all()
        totalbuy = sum([item.quantity for item in orderitems])
        totalrent = sum([item.quantity1 for item in rentitems])
        total = totalbuy + totalrent
        return total

class OrderItem(models.Model):
    """ Cart can have multiple item thats why we use foregnkey relationship """
    product = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True) # quantity of that book in cart, default is at 0
    date_added = models.DateTimeField(auto_now_add=True)
    
    @property
    # get total prices in cart for that book
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
class RentItem(models.Model):
    """ Cart can have multiple item thats why we use foregnkey relationship """
    product1 = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True)
    order1 = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity1 = models.IntegerField(default=0, null=True, blank=True) # quantity of that book in cart, default is at 0
    date_added1 = models.DateTimeField(auto_now_add=True)
    date_due1 = datetime.now() + timedelta(days=7)

class ReviewRating(models.Model):
    """ Review model for user with one to many relation ship, so one user can have write many reviews """
    
    user = models.ForeignKey(User, models.CASCADE)
    book = models.ForeignKey(Book, models.CASCADE, null=True)
    subject = models.TextField(max_length=100)
    review = models.TextField(max_length = 200)
    rate = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.rate)