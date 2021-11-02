from django import forms
from .models import User
from django.forms import ModelForm
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ["first_name", "last_name", "email", "username", "password", "confirm_password",
                  "music", "visual", "performing", "film", "lectures", "fashion",
                  "food", "festivals", "charity", "sports", "nightlife", "family"]
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput()
        }

    def clean(self):
        data = self.cleaned_data
        password = data.get("password")
        print("Is it this?")
        password_confirm = data.get("confirm_password")

        if password != password_confirm:
            raise ValidationError("Passwords did not match")

        #raise error for invalid input
        #get rid of submit button after user already there
        #how to retrieve user data
        return data


