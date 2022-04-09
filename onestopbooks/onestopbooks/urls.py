"""onestopbooks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from bookstore.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('aboutus/', aboutus_view, name='aboutus'),
    path('cart/', cart_view, name='cart'),
    path('books/', books_view, name='books'),
    path('newestbooks/', newestbooks_view, name='newestbooks'),
    path('booksunder/', booksunder_view, name='booksunder'),
    path('randombooks/', randombooks_view, name='randombooks'),
    path('checkout/', checkout_view, name='checkout'),
    path('bookstore/', include('bookstore.urls')),
    path('login/', loginPage, name='login'),
    path('signup/', signupPage, name='signup'),
    path('logout/', logoutPage,name='logout'),
    path('product/<str:isbn>', product_view, name='product'),
    path('update_item', update_item, name='update_item'),
    path('successcheckout/', successcheckout_view, name='successcheckout'),
    path('submit_review/<int:book_isbn>', submit_review, name='submit_review'),
]
