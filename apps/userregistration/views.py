from django.http import HttpResponse
from django.template import loader
from apps.userregistration.forms import Formregistration
from apps.userregistration.models import EN_UserRegistration


def index(request):
    template = loader.get_template("user_registration_page.html")
    data = {"form": Formregistration() if request.method!="POST" else Formregistration(request.POST)}
    return HttpResponse(template.render(data, request))
def Submitdata(request):
    form_data=Formregistration(request.POST)
    if form_data.is_valid():
        user_table=EN_UserRegistration()
        user_table.username=form_data.cleaned_data.get("username")
        user_table.password=form_data.cleaned_data.get("password")
        user_table.Name=form_data.cleaned_data.get("name")
        user_table.emailaddress=form_data.cleaned_data.get("emailname")
        user_table.save
        return HttpResponse("Saved the details")