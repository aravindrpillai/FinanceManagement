from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from util.static_data_loader import StaticDataLoader

def index(request):
    template = loader.get_template("category_homepage.html")
    data = StaticDataLoader(request).getPageData("is_category_home")
    return HttpResponse(template.render(data, request))

@csrf_exempt
def loadCategories(request):
    return HttpResponse("Hello")

@csrf_exempt
def saveCategory(request):
    category_name = request.POST.get("category_name")
    return HttpResponse(category_name)