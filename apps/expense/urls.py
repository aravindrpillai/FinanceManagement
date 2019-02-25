from django.urls import path
from . import views

urlpatterns = [
    path(r'',views.index, name="Renders Expense Page"),
    path(r'SaveExpense',views.saveExpense, name="Save Expense"),
]