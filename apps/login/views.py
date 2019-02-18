from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from apps.login.form import FORM_Login
from apps.userregistration.models import EN_Users

def index(request):
    template = loader.get_template("user_login_page.html")
    data = {"form":FORM_Login() if request.method!="POST"  else FORM_Login(request.POST)}
    return HttpResponse(template.render(data, request))

def validateLogin(request):
    if request.method == "POST":
        form_data=FORM_Login(request.POST)
        if form_data.is_valid():
            try:
                user = EN_Users.objects.get(username=request.POST.get('username'), password=request.POST.get('password'))
                request.session['userid']=user.id
                request.session['username']=user.name
                request.session['useremail']=user.email
                return HttpResponseRedirect("../Home")
            except Exception:
                messages.error(request, "Invalid Login Credentials")
                return index(request)
        else:
            return index(request)
    else:
        messages.error(request, "Direct Access Denied")
        return HttpResponseRedirect("../Login")
