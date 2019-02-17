from django.urls import path
from . import views

urlpatterns = [
    path(r'',views.index, name="Loads User Registration Page"),
    path(r'Submitdata',views.Submitdata,name="save_userregistration"),
]