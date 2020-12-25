from django import forms
from .models import Fruit

class FruitForm(forms.ModelForm):
    
    class Meta:
        model = Fruit
        fields = "__all__"
