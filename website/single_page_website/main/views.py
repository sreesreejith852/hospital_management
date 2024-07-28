from django.shortcuts import render


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, TaskForm
from .models import Task, User


def index(request):
    return render(request, 'main/index.html')

def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'main/index.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'main/login.html')

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'main/register.html', {'form': form})

@login_required
def dashboard(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    users = User.objects.all()
    return render(request, 'main/dashboard.html', {'tasks': tasks, 'users': users})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    form.fields['assigned_to'].queryset = User.objects.exclude(id=request.user.id)
    return render(request, 'main/add_task.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')
