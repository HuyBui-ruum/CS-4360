from django.contrib import admin
from .models import *

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    search_fields = ('isbn', 'title', 'authors', 'year_public', 'publisher',)

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'email', 'phone_number',)

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(RentItem)
admin.site.register(ReviewRating)
