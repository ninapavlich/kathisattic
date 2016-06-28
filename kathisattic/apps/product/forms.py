
from django import forms
from django.forms.widgets import CheckboxSelectMultiple

from models import *

class ProductCreateForm(forms.ModelForm):
    raw_image = forms.ImageField()


    class Meta:
        model = Product
        fields = ['title', 'suggested_price', 'content', 'tags']
        widgets = {"tags":CheckboxSelectMultiple(),}
