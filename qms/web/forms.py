
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

class LoginForm(forms.Form):
  
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"  username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"  password"}))
 


class SignUpForm(forms.ModelForm):
  
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"  password"}))
    passwordre = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":" confirm  password"}))
    companyname = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"company name"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"email address"}))
    mobile = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"mobile number"}))
    country = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"country"}))
    state = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"state"}))

    class Meta:
        model=User
        fields =('username','email')



    def clean(self):
        cleaned_data = super().clean()
        enter_password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("passwordre")

        if enter_password != confirm_password:
            raise forms.ValidationError(
                "please recheck password the _password does not match"
                )

    





                
      


