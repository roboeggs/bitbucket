from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import Employee
from .forms import LoginForm
from .register_forms import RegisterForm
from .profile_forms import ProfileEditForm

from django.urls import reverse

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse('login')  

    def form_valid(self, form):
        response = super().form_valid(form)
        # Логиним пользователя после успешной регистрации
        login(self.request, self.object.user)
        return response





@login_required
def edit_profile(request):
    user = request.user

    # Проверка наличия связанного объекта Employee у пользователя
    employee = user.employee.get(default=None)
    if employee is None:
        # Если у пользователя нет связанного объекта Employee, создаем его
        employee = Employee(user=user, hire_date=None)
        employee.save()

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Перенаправление на страницу профиля
    else:
        form = ProfileEditForm(instance=employee)

    return render(request, 'profile.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Authenticated successfully')
                    return redirect('employee_list')
                else:
                    messages.error(request, 'Disabled account')
            else:
                messages.error(request, 'Invalid login')
    else:
        form = LoginForm()

    # Проверка, зарегистрирован ли пользователь
    if request.user.is_authenticated:
        return redirect('employee_list')

    return render(request, 'registration/login.html', {'form': form})

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

def employee_hierarchy(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_hierarchy.html', {'employees': employees})

@method_decorator(login_required, name='get')
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'
    ordering = ['-hire_date']

    def get_queryset(self):
        # Проверка, зарегистрирован ли пользователь
        if not self.request.user.is_authenticated:
            # Если не зарегистрирован, вы можете добавить свою логику обработки
            # например, перенаправить на страницу входа или показать сообщение об ошибке
            return Employee.objects.none()

        sort_param = self.request.GET.get('sort')
        if sort_param:
            return Employee.objects.all().order_by(sort_param)
        return super().get_queryset()
