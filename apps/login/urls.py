from django.urls import path
from . import views

urlpatterns = [
    path(r'',views.index, name="User Login Page"),
    path(r'Submitlogdata',views.Submitlogdata,name="submitlogdata"),
]