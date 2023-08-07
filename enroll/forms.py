from django import forms
from.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'idNo', 'email', 'password', 'salary']
        widgets = {
          'name': forms.TextInput(attrs={'class': 'ms-4'}),
          'idNo': forms.NumberInput(attrs={'class': 'ms-4'}),
          'email': forms.EmailInput(attrs={'class': 'ms-4'}),
          'password': forms.PasswordInput(attrs={'class': 'ms-1'}),
          'salary': forms.NumberInput(attrs={'class': 'ms-4'}),
        }
