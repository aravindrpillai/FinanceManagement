import json
from django.http import HttpResponse, HttpResponseRedirect
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
    if request.is_ajax():
        categoryList = [{
          "id" : category.id,
          "name" : category.name
        }for category in EN_Categories.objects.filter(user_id=request.session[SessionProperties.USER_ID], retired=False).order_by('name')]
        return HttpResponse(json.dumps(categoryList))
    else:
        return HttpResponseRedirect("../Categories")


@csrf_exempt
def saveCategory(request):
    if request.is_ajax():
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
    else:
        return HttpResponseRedirect("../Categories")


@csrf_exempt
def deleteCategory(request):
    if request.is_ajax():
        try:
            id = request.POST.get("id")
            if id == "" or id == None:
                raise Exception("Invalid category selected")
            if(not EN_Categories.objects.filter(id=int(id), user_id=request.session[SessionProperties.USER_ID], retired=False).exists()):
                raise Exception("Category does not exist")
            else:
                cat = EN_Categories.objects.get(id=int(id))
                cat.retired = True
                cat.save()
                subCat = EN_SubCategories.objects.get(category=cat)
                subCat.retired = True
                subCat.save()
                return HttpResponse(1)
        except Exception as e:
            return HttpResponse(e.__str__())
    else:
        return HttpResponseRedirect("../Categories")


@csrf_exempt
def loadSubCategories(request):
    if request.is_ajax():
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
    else:
        return HttpResponseRedirect("../Categories")


@csrf_exempt
def deleteSubCategory(request):
    if request.is_ajax():
        try:
            id = request.POST.get("id")
            if id == "" or id == None:
                raise Exception("Invalid category selected")
            if(not EN_SubCategories.objects.filter(id=int(id), user_id=request.session[SessionProperties.USER_ID], retired=False).exists()):
                raise Exception("Category does not exist")
            else:
                subCat = EN_SubCategories.objects.get(id=int(id))
                subCat.retired = True
                subCat.save()
            return HttpResponse(1)
        except Exception as e:
            return HttpResponse(e.__str__())
    else:
        return HttpResponseRedirect("../Categories")



@csrf_exempt
def saveSubCategory(request):
    if request.is_ajax():
        try:
            category_id = request.POST.get("category_id")
            sub_category_name = request.POST.get("sub_category_name")
            if sub_category_name == "" or sub_category_name== None:
                raise Exception("SubCategory cannot be empty")
            if (not EN_Categories.objects.filter(id=int(category_id), user_id=request.session[SessionProperties.USER_ID],retired=False).exists()):
                raise Exception("Category does not exists")
            if(EN_SubCategories.objects.filter(name=sub_category_name, user_id=request.session[SessionProperties.USER_ID], retired=False).exists()):
                raise Exception("SubCategory already exists")
            subCategory = EN_SubCategories()
            subCategory.category_id = int(category_id)
            subCategory.name = sub_category_name
            subCategory.user_id = request.session[SessionProperties.USER_ID]
            subCategory.save()
            return HttpResponse(1)
        except Exception as e:
            return HttpResponse(e.__str__())
    else:
        return HttpResponseRedirect("../Categories")

