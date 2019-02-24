from django.urls import path
from . import views

urlpatterns = [
    path(r'',views.index, name="Renders Home Page"),
    path(r'LoadCategories',views.loadCategories, name="Load categories of user"),
    path(r'SaveCategory',views.saveCategory, name="Save category and return to same page"),
]