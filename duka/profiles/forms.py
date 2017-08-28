from __future__ import unicode_literals
from authtools import forms as authtoolsforms
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django.contrib.auth import get_user_model
from .models import Collector

User = get_user_model()


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
