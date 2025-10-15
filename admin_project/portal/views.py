from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Employee, LeaveRequest
from django.contrib import messages

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboard View
@login_required
def dashboard_view(request):
    employee_count = Employee.objects.count()
    leave_count = LeaveRequest.objects.count()
    pending_leave_count = LeaveRequest.objects.filter(status='Pending').count()
    
    context = {
        'employee_count': employee_count,
        'leave_count': leave_count,
        'pending_leave_count': pending_leave_count
    }
    return render(request, 'index.html', context)

# Employee Management View
@login_required
def employees_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        role = request.POST.get('role')
        department = request.POST.get('department')
        Employee.objects.create(name=name, role=role, department=department)
        return redirect('employees')
        
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})

# Leave Management View
@login_required
def leave_management_view(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        leave_type = request.POST.get('leave_type')
        
        employee = Employee.objects.get(id=employee_id)
        LeaveRequest.objects.create(
            employee=employee,
            start_date=start_date,
            end_date=end_date,
            leave_type=leave_type
        )
        return redirect('leave_management')

    employees = Employee.objects.all()
    leaves = LeaveRequest.objects.all().order_by('-id')
    return render(request, 'leave_management.html', {'leaves': leaves, 'employees': employees})
    
# Other static pages
@login_required
def attendance_view(request):
    return render(request, 'attendance.html')

@login_required
def salary_view(request):
    return render(request, 'salary.html')

@login_required
def departments_view(request):
    return render(request, 'departments.html')

@login_required
def reports_view(request):
    return render(request, 'reports.html')
