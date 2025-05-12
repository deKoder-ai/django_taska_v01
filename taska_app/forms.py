from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Project
from django.utils import timezone

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)  # Add any other fields you need

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set initial due_date to one week from today
        self.initial['due_date'] = timezone.now() + timezone.timedelta(days=7)