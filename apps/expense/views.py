import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from apps.categories.models import EN_Categories, EN_SubCategories
from apps.expense.models import EN_Expenses
from properties.session_properties import SessionProperties
from util.static_data_loader import StaticDataLoader


def index(request):
    template = loader.get_template("expense_homepage.html")
    data = StaticDataLoader(request).getPageData("is_expense")
    return HttpResponse(template.render(data, request))

def saveExpense(request):
    if request.is_ajax():
        try:
            category_id = request.POST.get("category_id")
            if category_id == "" or category_id == None:
                raise Exception("Invalid category")
            elif not EN_Categories.objects.filter(id=int(category_id), user_id=request.session[SessionProperties.USER_ID]).exists():
                raise Exception("Invalid category")
            else:
                category_id = int(category_id)

            sub_category_id = request.POST.get("sub_category_id")
            if sub_category_id == "" or sub_category_id == None:
                sub_category_id = None
            elif not EN_SubCategories.objects.filter(id=int(sub_category_id), category_id = int(category_id),user_id=request.session[SessionProperties.USER_ID]).exists():
                raise Exception("SubCategory doesn't belongs to selected category")
            else:
                sub_category_id = int(sub_category_id)

            amount = request.POST.get("amount")
            if amount == "" or amount == None:
                raise Exception("Invalid amount")
            elif float(amount) < 0.01:
                raise Exception("Amount cannot be less than 0.01 Rs")
            else:
                amount = float(amount)

            description = request.POST.get("description")
            if description == None or description == "":
                description = None

            expense_date = request.POST.get("expense_date")
            if expense_date == None or expense_date == "":
                expense_date = datetime.datetime.now()
            else:
                datetime.datetime.strptime(expense_date,"%m/%d/%Y")

            exp =  EN_Expenses()
            exp.category_id = category_id
            exp.sub_category_id = sub_category_id
            exp.amount = amount
            exp.description = description
            exp.date = expense_date
            exp.save()
            return HttpResponse(1)

        except Exception as e:
            return HttpResponse(e.__str__())
    else:
        return HttpResponseRedirect("../Home")