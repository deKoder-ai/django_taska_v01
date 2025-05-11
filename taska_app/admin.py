from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from .models import User, Project, Task

from django.urls import reverse
from django.utils.html import format_html

@admin.action(description='Deactivate selected users')
def deactivate_users(modeladmin, request, queryset):
    queryset.update(is_active=False)
    messages.success(request, f"{queryset.count()} users were deactivated")

@admin.action(description='Activate selected users')
def activate_users(modeladmin, request, queryset):
    queryset.update(is_active=True)
    messages.success(request, f"{queryset.count()} users were activated")

@admin.action(description='Permanently delete selected users')
def hard_delete_users(modeladmin, request, queryset):
    count = queryset.count()
    queryset.delete()
    messages.success(request, f"{count} users were permanently deleted")

class CustomUserAdmin(UserAdmin):
    actions = [deactivate_users, activate_users, hard_delete_users]
    
    list_display = ('username', 'email', 'is_active', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.has_perm('taska_app.can_undelete'):
            return qs
        return qs.filter(is_active=True)
    
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        user = User.objects.get(pk=object_id)
    
        extra_context['show_delete'] = not user.is_superuser or request.user.is_superuser
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

    def delete_view(self, request, object_id, extra_context=None):
        if request.method == 'POST':
            user = User.objects.get(pk=object_id)
            if not user.is_superuser or request.user.is_superuser:
                user.delete()
                messages.success(request, 'User was permanently deleted')
            else:
                messages.error(request, 'Cannot delete superusers')
        return super().delete_view(request, object_id, extra_context)

admin.site.register(User, CustomUserAdmin)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'due_date', 'created_date')
    list_filter = ('user', 'due_date')
    search_fields = ('title', 'user__username')
    date_hierarchy = 'due_date'
    
    # Show only current user's projects in dropdown (for staff users)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    # Set current user as default when creating projects
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
        super().save_model(request, obj, form, change)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'priority', 'due_date', 'completed')
    list_filter = ('project', 'priority', 'completed', 'frequency')
    search_fields = ('title', 'project__title', 'description')
    date_hierarchy = 'due_date'
    list_editable = ('completed',)  # Allows bulk editing
    raw_id_fields = ('project',)  # Better for large project lists
    
    # Show priority as colored labels
    @admin.display(description='Priority')
    def colored_priority(self, obj):
        colors = {
            'C': 'red',
            'H': 'orange',
            'M': 'yellow',
            'L': 'green',
            'Z': 'gray'
        }
        return format_html(
            '<span style="color: {};">{}</span>',
            colors.get(obj.priority, 'black'),
            obj.get_priority_display()
        )