from django.urls import path
from . import views

urlpatterns = [
    path(r'',views.index, name="Renders Home Page"),
    path(r'LoadCategories',views.loadCategories, name="Load categories of user"),
    path(r'SaveCategory',views.saveCategory, name="Save category and return to same page"),
    path(r'DeleteCategory',views.deleteCategory, name="Delete category and return to same page"),
    path(r'LoadSubCategories',views.loadSubCategories, name="Load sub categories and return to same page"),
]