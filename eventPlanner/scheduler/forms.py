from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password",
                  "music", "visual", "performing", "film", "lectures", "fashion",
                  "food", "festivals", "charity", "sports", "nightlife", "family"]
