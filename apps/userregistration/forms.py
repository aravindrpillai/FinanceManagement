from django import forms
from apps.userregistration.models import EN_Users

class FORM_UserRegistration(forms.Form):

    name = forms.CharField(min_length=5,max_length=25,required=True)
    username = forms.CharField(min_length=5,required=True)
    password = forms.CharField(min_length=6,required=True)
    email = forms.EmailField(required=True)

    def clean(self):
        data=self.cleaned_data
        if data["username"] is None:
            self.add_error("username","Username is required")
        elif EN_Users.objects.filter(username=data["username"]).exists():
            self.add_error("username","Username already exists")

        if data["name"] is None:
            self.add_error("name","Name is required")

        if data["password"] is None:
            self.add_error("password","Password is required")

        if data["email"] is None:
            self.add_error("email","Email is required")
        elif EN_Users.objects.filter(email=data["email"]).exists():
            self.add_error("email", "Email ID already exists")

        return data

