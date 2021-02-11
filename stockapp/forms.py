from django import forms
from .models import orders5
class new_order(forms.ModelForm):
    class Meta:
        model = orders5
        fields = '__all__' 

    