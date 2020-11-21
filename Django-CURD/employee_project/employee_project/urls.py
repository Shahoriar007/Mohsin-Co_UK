from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('employee_register.urls')),
]

handler404 = 'employee_register.views.error_404_view'