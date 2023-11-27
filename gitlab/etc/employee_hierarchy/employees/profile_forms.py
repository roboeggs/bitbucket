# myapp/forms.py
from django import forms
from .models import Employee

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name', 'position', 'hire_date', 'salary', 'photo']