from django import forms
from apps.userregistration.models import EN_UserRegistration
class Formregistration(forms.Form):
    Name=forms.CharField(min_length=5,max_length=25,required=True)
    username=forms.CharField(min_length=5,required=True)
    password=forms.CharField(min_length=6,required=True)
    emailname=forms.EmailField(required=True)

    def clean(self):
        data=self.cleaned_data
        username=data["username"]
        name=data["Name"]
        password=data["password"]
        emailname=data["emailname"]
        if username is None:
            self.add_error("username","username is required")
        elif name is None:
            self.add_error("Name","Name is required")
        elif password is None:
            self.add_error("password","password is required")
        elif emailname is None:
            self.add_error("emailname","emailname is required")

        return data

