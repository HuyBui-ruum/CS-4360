from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    """ Create user form """
    class Meta:
        model=User
        fields=['username', 'password1', 'password2']

class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['user']

class ReviewRatingForm(ModelForm):
    """ Create form for review and rating """
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rate']

