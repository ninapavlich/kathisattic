
from django import forms
from django.forms.widgets import CheckboxSelectMultiple

from models import *

class ProductCreateForm(forms.ModelForm):
    raw_image = forms.ImageField()


    class Meta:
        model = Product
        fields = ['title', 'suggested_price',  'sale_status', 'tags', 'condition', 'length', 'width', 'height', 'weight', 'content',]
        widgets = {"tags":CheckboxSelectMultiple(),}

    
