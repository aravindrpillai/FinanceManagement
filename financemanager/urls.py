from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'UserRegistration/', include("apps.userregistration.urls")),
    path(r'Login/', include("apps.login.urls")),
    path(r'Home/', include("apps.home.urls")),
    path(r'Expense/', include("apps.expense.urls")),
    path(r'Categories/', include("apps.categories.urls")),

]
