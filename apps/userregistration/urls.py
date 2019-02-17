from django.urls import path
from . import views

urlpatterns = [
    path(r'',views.index, name="Loads User Registration Page"),
    path(r'Submitdata',views.submitData,name="Saves User Registration Data To DB"),
]