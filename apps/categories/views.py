from django.http import HttpResponse
from django.template import loader
from util.static_data_loader import StaticDataLoader

def index(request):
    template = loader.get_template("category_homepage.html")
    data = StaticDataLoader(request).getPageData("is_category_home")
    return HttpResponse(template.render(data, request))

