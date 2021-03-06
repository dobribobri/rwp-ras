
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('birth_date', 'sex', 'phone', 'education', 'degree', 'title')
