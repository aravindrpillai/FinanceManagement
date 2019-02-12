from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("user_login_page.html")
    data = {}
    return HttpResponse(template.render(data, request))
