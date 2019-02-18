from django.contrib import messages
from django.http import HttpResponseRedirect

#Authentication

class MW_Authentication():
    excluded_apps=["Login",
                   "UserRegistration",
    ]

    def __init__(self,get_response):
         self.get_response=get_response
    def __call__(self,request):
        appname=request.path.split("/")[1]
        if appname not in self.excluded_apps:
            user_id=request.session['userid']
            if user_id == None:
            #Logger.error("Middleware Authentication Denied User ID {} To Access App {} ".format(user_id, appName))
               messages.warning(request, "error_session_time_out")
               return HttpResponseRedirect("../Login")
        return self.get_response(request)