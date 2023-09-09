from .models import student_info
from django import forms

class data(forms.ModelForm):
    class Meta:
        model = student_info
        fields = '__all__'
