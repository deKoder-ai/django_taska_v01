from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import CustomUserCreationForm, ProjectForm
from .models import Project

def index(request):
    """Handle root URL - shows taska if authenticated, else redirects to login"""
    if request.user.is_authenticated:
        projects = Project.objects.filter(user=request.user).order_by('due_date')
        return render(request, 'taska_app/taska.html', {'projects': projects})
    return redirect('login')

def register(request):
    """Handle user registration"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'taska_app/register.html', {'form': form})

@login_required
def create_project(request):
    """Handle project creation"""
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('index')
    else:
        form = ProjectForm()
    return render(request, 'taska_app/new_project.html', {'form': form})