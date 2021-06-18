from django.forms import ModelForm
from .models import *

class OrderForm1(ModelForm):
	class Meta:
		model = Product
		fields = ['name','description']

class OrderForm(ModelForm):
    class Meta:
        model=Orders
        fields='__all__'
