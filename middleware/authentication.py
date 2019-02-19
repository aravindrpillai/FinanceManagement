from django.contrib import messages
from django.http import HttpResponseRedirect
from properties.session_properties import SessionProperties

class MW_Authentication():
    excluded_apps=["Login","UserRegistration"]

    def __init__(self,get_response):
         self.get_response=get_response

    def __call__(self,request):
        appname=request.path.split("/")[1]
        if appname not in self.excluded_apps:
            if not SessionProperties.USER_ID in request.session:
                messages.warning(request, "error_session_time_out")
                return HttpResponseRedirect("../Login")
            else:
                if request.session[SessionProperties.USER_ID] == None:
                   messages.warning(request, "error_session_time_out")
                   return HttpResponseRedirect("../Login")
        return self.get_response(request)