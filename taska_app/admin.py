from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from .models import User

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

