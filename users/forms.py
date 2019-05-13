from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile                                     # This is imported to operate on profile image in UserUpdateForm class below.

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class  UserUpdateForm(forms.ModelForm):                         # As we have created UserRegisteration form above we are going to create Update form for the user info
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']