from dataclasses import fields
from django import forms
from .models import Employee_details, New_Employee

class New_Emp(forms.ModelForm):
    class Meta:
        model = New_Employee
        fields = "__all__"

class Employee_details_forms(forms.ModelForm):
    class Meta:
        model = Employee_details
        fields = "__all__"