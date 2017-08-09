#coding: utf8
from django import forms
from models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product

    def __init__(self,*args, **kwargs):
        super(ProductForm,self).__init__(*args,**kwargs)

    def clean_price(self):
        price=self.cleaned_date['price']
        if price<=0:
            raise forms.validationError("价格必须大于0")
        return price