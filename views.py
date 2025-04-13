# proctoring/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from .models import UserProfile, Violation
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about_us.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            UserProfile.objects.create(user=user, role=form.cleaned_data['role'])
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                role = user.userprofile.role
                return redirect('admin_dashboard' if role == 'admin' else 'student_dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return render(request,'logout.html')

@login_required
def admin_dashboard(request):
    return render(request,'admin.html')

@login_required
def student_dashboard(request):
    return render(request,'student.html')

@login_required
def exam_page(request):
    return render(request, 'proctoring/exam_page.html')

@login_required
def violation_log(request):
    violations = Violation.objects.filter(user=request.user) if request.user.userprofile.role == 'student' else Violation.objects.all()
    return render(request, 'proctoring/violation.html', {'violations': violations})# proctoring/urls.py


