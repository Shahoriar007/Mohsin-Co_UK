from django.urls import path,include
from . import views
#from django.conf.urls import handler404

urlpatterns = [
    
    path('services/', views.employee_form,name='employee_insert'),
    path('about/',views.aboutPage,name='about'),
    path('',views.servicesPage,name='services'),
    path('contact/',views.contactPage,name='contact'),
    path('faq/',views.faqPage,name='faq'),
    path('testimonial/',views.testimonialPage,name='testimonial'),

    path('<int:id>/', views.employee_form,name='employee_update'), # get and post req. for update operation
    path('list/',views.employee_list,name='employee_list'),
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),

    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout')
]

#handler404 = ''