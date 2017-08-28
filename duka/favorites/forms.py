from django import forms
from . models import Favorite

class FavoriteCreateForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = ('name', 'age_bracket', 'drink', 'location')