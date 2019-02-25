import json

from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from apps.categories.models import EN_Categories, EN_SubCategories
from properties.session_properties import SessionProperties
from util.static_data_loader import StaticDataLoader

def index(request):
    template = loader.get_template("category_homepage.html")
    data = StaticDataLoader(request).getPageData("is_category_home")
    return HttpResponse(template.render(data, request))

@csrf_exempt
def loadCategories(request):
    categoryList = [{
      "id" : category.id,
      "name" : category.name
    }for category in EN_Categories.objects.filter(user_id=request.session[SessionProperties.USER_ID], retired=False).order_by('name')]
    return HttpResponse(json.dumps(categoryList))

@csrf_exempt
def saveCategory(request):
    try:
        category_name = request.POST.get("category_name")
        if category_name == "" or category_name == None:
            raise Exception("Category cannot be empty")
        if(EN_Categories.objects.filter(name=category_name, user_id=request.session[SessionProperties.USER_ID], retired=False).exists()):
            raise Exception("Category already exists")
        category = EN_Categories()
        category.name = category_name
        category.user_id = request.session[SessionProperties.USER_ID]
        category.save()
        return HttpResponse(1)
    except Exception as e:
        return HttpResponse(e.__str__())


@csrf_exempt
def deleteCategory(request):
    try:
        id = request.POST.get("id")
        if id == "" or id == None:
            raise Exception("Invalid category selected")
        if(not EN_Categories.objects.filter(id=int(id), user_id=request.session[SessionProperties.USER_ID], retired=False).exists()):
            raise Exception("Category does not exist")
        else:
            EN_Categories.objects.get(id=int(id)).delete()
        return HttpResponse(1)
    except Exception as e:
        return HttpResponse(e.__str__())


@csrf_exempt
def loadSubCategories(request):
    try:
        categoryId = request.POST.get("id")
        if categoryId == "" or categoryId == None:
            raise Exception("Invalid category")
        if (not EN_Categories.objects.filter(id=int(categoryId), user_id=request.session[SessionProperties.USER_ID],retired=False).exists()):
            raise Exception("Invalid category")
        subCategoryList = [{
          "id" : subCategory.id,
          "name" : subCategory.name
        }for subCategory in EN_SubCategories.objects.filter(category_id=int(categoryId),user=request.session[SessionProperties.USER_ID], retired=False).order_by('name')]
        return HttpResponse(json.dumps(subCategoryList))
    except:
        return HttpResponse(0)