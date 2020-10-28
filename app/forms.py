from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Category, Product


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [
            'category',
            'image',
            'active',
        ]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'category',
            'name',
            'description',
            'price',
            'image_1',
            'image_2',
            'image_3',
            'image_4',
            'image_5',
            'image_6',
            'active',
        ]


class WorkForceRegistrationForm(UserCreationForm):   # Tested and PWNE
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
            'is_staff',
        ]
