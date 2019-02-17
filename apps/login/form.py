from django import forms

class FORM_Login(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)

    def clean(self):
      data=self.cleaned_data
      return data