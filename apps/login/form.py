from apps.userregistration.models import EN_UserRegistration
from django import forms
class Formlogin(forms.Form):
    Email=forms.EmailField(required=True)
    Password=forms.CharField(required=True)
    def clean(self):
      data=self.cleaned_data
      email=data["Email"]
      Password=data["Password"]
      if email is None:
        self.add_error("email","email is required")
      if Password is None:
        self.add_error("Password","password is required")

      return data