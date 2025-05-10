from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model

class User(AbstractUser):
  is_active = models.BooleanField(
    default=True,
    help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'
  )

  def soft_delete(self):
    """Deactivate user instead of deleting"""
    self.is_active = False
    self.save()

  class Meta:
    permissions = [
      ('can_undelete', 'Can restore deleted users'),
    ]

# task models
User = get_user_model()

def one_week_hence():
  return timezone.now() + timezone.timedelta(days=7)

class TaskList(models.Model):
  title = models.CharField(max_length=100, unique=True)
  created_date = models.DateTimeField(auto_now_add=True)

  def get_absolute_url(self):
    return reverse('list', args=[self.id])

  def __str__(self):
    return self.title

class TaskItem(models.Model):
  # Priority Choices
  PRIORITY_CHOICES = [
    ('C', 'Critical'),
    ('H', 'High'),
    ('M', 'Medium'),
    ('L', 'Low'),
    ('Z', 'Zero'),
  ]
  
  # Frequency Choices (renamed from Recurrence)
  FREQUENCY_CHOICES = [
    ('N', 'None'),
    ('D', 'Daily'),
    ('W', 'Weekly'),
    ('M', 'Monthly'),
    ('Y', 'Yearly'),
  ]

  # Core Fields
  title = models.CharField(max_length=100)
  description = models.TextField(null=True, blank=True)
  notes = models.TextField(null=True, blank=True)
  created_date = models.DateTimeField(auto_now_add=True)
  due_date = models.DateTimeField(default=one_week_hence)
  completed = models.BooleanField(default=False)
  completed_date = models.DateTimeField(null=True, blank=True)
  task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
  
  # New Fields
  priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
  frequency = models.CharField(max_length=1, choices=FREQUENCY_CHOICES, default='N')  # Renamed
  attachment = models.FileField(upload_to='task_attachments/', null=True, blank=True)
  last_modified = models.DateTimeField(auto_now=True)
  author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Renamed
  color = models.CharField(max_length=7, default='#FFFFFF')

  def get_absolute_url(self):
    return reverse('item-update', args=[str(self.task_list.id), str(self.id)])

  def __str__(self):
    return f'{self.title}: due {self.due_date}'

  class Meta:
    ordering = ['due_date']