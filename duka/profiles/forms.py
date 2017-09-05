from __future__ import unicode_literals
from authtools import forms as authtoolsforms
from django import forms
from django.contrib.auth import get_user_model
from .models import Collector

User = get_user_model()

class JoinForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=120)

class CollectorCreateForm(authtoolsforms.UserCreationForm):
    pass

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name']


class CollectorForm(forms.ModelForm):
    class Meta:
        model = Collector
        fields = ('collector_no', 'phone', 'id_no', 'centre', 'gender')
