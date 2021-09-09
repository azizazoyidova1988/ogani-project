from django import forms
from .models import Category, Product, User_Address,Send_Message

class User_AddressForm(forms.ModelForm):
    class Meta:
        model = User_Address()
        fields = '__all__'

class Send_MessageForm(forms.ModelForm):
    class Meta:
        model=Send_Message()
        fields='__all__'