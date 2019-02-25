from django.http import HttpResponse
from django.template import loader
from util.static_data_loader import StaticDataLoader


def index(request):
    template = loader.get_template("expense_homepage.html")
    data = StaticDataLoader(request).getPageData("is_expense")
    return HttpResponse(template.render(data, request))
