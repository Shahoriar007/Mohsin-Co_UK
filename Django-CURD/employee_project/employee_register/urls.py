from django.urls import path,include
from . import views


urlpatterns = [
    
    path('book-appointment/', views.employee_form,name='employee_insert'),
    path('services/', views.allservices,name='all_services'),
    path('about/',views.aboutPage,name='about'),
    path('',views.servicesPage,name='services'),
    path('contact/',views.contactPage,name='contact'),
    path('faq/',views.faqPage,name='faq'),
    path('testimonial/',views.testimonialPage,name='testimonial'),

    # Service Details Pages
    path('business-start-ups/',views.advisoryforstartups,name='advisory_for_startups'),
    path('bookkeeping/',views.bookkeeping,name='bookkeeping'),
    path('investigation/',views.investigation,name='investigation'),
    path('enrollment-for-pensions/',views.AutomaticEnrollment,name='AutomaticEnrollment'),
    path('company-secretarial-&-other/',views.CompanySecretarial,name='CompanySecretarial'),
    path('payroll-&-RTI-submission/',views.Payroll,name='Payroll'),
    path('statutory-accounts/',views.StatutoryAccounts,name='StatutoryAccounts'),
    # path('VAT/',views.VAT,name='VAT'),
    path('tax-planning/',views.Tax,name='Tax'),

    path('<int:id>/', views.employee_form,name='employee_update'),
    path('list/',views.employee_list,name='employee_list'),
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),

    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),


    
]

