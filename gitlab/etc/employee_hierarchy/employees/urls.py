from django.urls import path
from .views import employee_hierarchy, EmployeeListView, user_login, RegisterView, employee_list, edit_profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('employee_hierarchy/', employee_hierarchy, name='employee_hierarchy'),
    path('employee_list/', EmployeeListView.as_view(), name='employee_list'),
    # path('employee_list/', employee_list, name='employee_list'),
    # path('employee_list/', EmployeeListView.as_view(), name='employee_list'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', user_login, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('profile/', edit_profile, name='profile'),
]
