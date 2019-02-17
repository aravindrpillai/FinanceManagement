from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from apps.userregistration.forms import FORM_UserRegistration
from apps.userregistration.models import EN_Users

def index(request):
    template = loader.get_template("user_registration_page.html")
    data = {"form": FORM_UserRegistration() if request.method!="POST" else FORM_UserRegistration(request.POST)}
    return HttpResponse(template.render(data, request))

def submitData(request):
    if request.method == "POST":
        form_data=FORM_UserRegistration(request.POST)
        if form_data.is_valid():
            try:
                user_table = EN_Users()
                user_table.username = form_data.cleaned_data.get("username")
                user_table.password = form_data.cleaned_data.get("password")
                user_table.Name = form_data.cleaned_data.get("name")
                user_table.email = form_data.cleaned_data.get("email")
                user_table.save()
                messages.success(request,"Successfully registered")
                return HttpResponseRedirect("../Login")
            except Exception as e:
                messages.error(request, "Faile to register : {}".format(e.__str__()))
                return index(request)
        else:
            return index(request)
    else:
        messages.error(request, "Direct access denied")
        return HttpResponseRedirect("../UserRegistration")
