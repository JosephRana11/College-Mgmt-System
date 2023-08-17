from users.models import CustomUser
from django import forms


class UserLoginForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ["email" , "password"]