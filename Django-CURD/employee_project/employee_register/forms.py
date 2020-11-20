from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = '__all__' #Show all fields 
        fields = ('fullname', 'emp_code', 'nature', 'mobile', 'email', 'position') #show selected fields
        labels = {                                  #fields name change
            'fullname':'Company Name',
            'emp_code':'Registration No',
            'nature': 'Nature of Business',
            'mobile': 'Business Contact No',
            'email': 'Business Email',
            'position': 'Service Needed',
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        #self.fields['emp_code'].required = False    #Change in Requird 

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']