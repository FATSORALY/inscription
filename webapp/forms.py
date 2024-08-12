from django.contrib.auth.forms import UserCreationForm #manome halalana micreer utilisateur
from django.contrib.auth.models import User
from django.contrib.auth.models import auth

from .models import Record
 
from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

#--register/Crete a user

class CreateUserForm(UserCreationForm):



    class Meta: 
        
        model = User
        fields = ['username', 'password1', 'password2']


#--Login a User

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
#-- Add reccord  
class CreateRecordForm(forms.ModelForm):
    
    class Meta: 
        
        model = Record
        fields = ['first_name', 'last_name', 'email','phone', 'address','city', 'province','country']
    
#-- Update reccord  
class UpdateRecordForm(forms.ModelForm):
    
    class Meta: 
        
        model = Record
        fields = ['first_name', 'last_name', 'email','phone', 'address','city', 'province','country']
    


