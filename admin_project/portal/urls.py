from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Core
    path('', views.dashboard_view, name='dashboard'),
    path('employees/', views.employees_view, name='employees'),
    path('leave/', views.leave_management_view, name='leave_management'),
    
    # Static pages
    path('attendance/', views.attendance_view, name='attendance'),
    path('salary/', views.salary_view, name='salary'),
    path('departments/', views.departments_view, name='departments'),
    path('reports/', views.reports_view, name='reports'),
]