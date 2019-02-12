from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'UserRegistration/', include("apps.userregistration.urls")),
    path(r'Login/', include("apps.login.urls")),

]
