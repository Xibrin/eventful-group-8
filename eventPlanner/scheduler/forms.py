from django import forms
from .models import User
from django.forms import ModelForm
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ["first_name", "last_name", "email", "username", "password", "confirm_password",  "city", "state",
                  "music", "visual", "performing", "film", "lectures", "fashion",
                  "food", "festivals", "charity", "sports", "nightlife", "family"]
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput()
        }

    def clean(self):
        data = self.cleaned_data
        password = data.get("password")
        #print("Is it this?")
        password_confirm = data.get("confirm_password")

        if password != password_confirm:
            raise ValidationError("Passwords did not match")

        #get rid of submit button after user already there
        #how to retrieve user data
        music = data.get("music")
        visual = data.get("visual")
        performing = data.get("performing")
        film = data.get("film")
        lectures = data.get("lectures")
        fashion = data.get("fashion")
        food = data.get("food")
        festivals = data.get("festivals")
        charity = data.get("charity")
        sports = data.get("sports")
        nightlife = data.get("nightlife")
        family = data.get("family")

        if music > 10:
            raise ValidationError("You cannot rate higher than 10")
        if visual > 10:
            raise ValidationError("You cannot rate higher than 10")
        if performing > 10:
            raise ValidationError("You cannot rate higher than 10")
        if film > 10:
            raise ValidationError("You cannot rate higher than 10")
        if lectures > 10:
            raise ValidationError("You cannot rate higher than 10")
        if fashion > 10:
            raise ValidationError("You cannot rate higher than 10")
        if food > 10:
            raise ValidationError("You cannot rate higher than 10")
        if festivals > 10:
            raise ValidationError("You cannot rate higher than 10")
        if charity > 10:
            raise ValidationError("You cannot rate higher than 10")
        if sports > 9:
            raise ValidationError("You cannot rate higher than 10")
        if nightlife > 10:
            raise ValidationError("You cannot rate higher than 10")
        if family > 10:
            raise ValidationError("You cannot rate higher than 10")
        return data





