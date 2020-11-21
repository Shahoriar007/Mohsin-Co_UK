from django.shortcuts import render, redirect
from .forms import EmployeeForm, CreateUserForm
from .models import Employee
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('employee_list')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('employee_list')
            else:
                messages.info(request, 'Username OR Password Incorrect')

        context = {}
        return render(request, "employee_register/login.html", context)

@login_required(login_url='login')
def registerPage(request):
    form = CreateUserForm()
    #if request.user.is_authenticated:
    #   return redirect('login')
    #else:
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)


            return redirect('login')

    context = {'form':form}
    return render(request, "employee_register/register.html", context)


def logoutUser(request):
    logout(request)
    return redirect('employee_insert')

@login_required(login_url='login')
def employee_list(request):
    context = {"employee_list" : Employee.objects.all()}
    return render(request,"employee_register/employee_list.html",context)

def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('employee_insert')

@login_required(login_url='login')
def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employee_list')

def aboutPage(request):
    return render(request, 'employee_register/about.html')

def servicesPage(request):
    return render(request, 'employee_register/base.html')

def contactPage(request):
    return render(request, 'employee_register/contact.html')

def faqPage(request):
    return render(request, 'employee_register/faq.html')

def testimonialPage(request):
    return render(request, 'employee_register/testimonial.html')

def error_404_view(request, exception):
     return render(request, 'employee_register/404.html')

