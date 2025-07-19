from django.contrib.auth.forms import UserCreationForm
from users.models import User
from django import forms


class RegisterUser(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("bio", "birth_date", "first_name", "last_name")
