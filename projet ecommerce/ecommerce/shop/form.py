from django import forms
from .models import Product
# pour authentification
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['nom','description','categorie','prix','quantite_en_stock','image']