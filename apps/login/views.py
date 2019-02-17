from django.http import HttpResponse
from django.template import loader
from apps.login.form import Formlogin
from apps.userregistration.models import EN_UserRegistration
def index(request):
    template = loader.get_template("user_login_page.html")
    data = {"form":Formlogin() if request.method!="POST"  else Formlogin(request.POST)}
    return HttpResponse(template.render(data, request))
def Submitlogdata(request):
    form_data=Formlogin(request.POST)
    if form_data.is_valid():
        if not EN_UserRegistration.objects.filter(username=form_data["Email"],password=form_data["Password"]):
         return Submitlogdata(request.POST)
        else:
         return("good job")