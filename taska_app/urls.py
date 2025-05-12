from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Main view
    path('', views.index, name='index'),
    
    # Auth URLs
    path('accounts/login/', 
          auth_views.LoginView.as_view(
            template_name='taska_app/login.html', 
            redirect_authenticated_user=True
          ), 
         name='login'),
    path('accounts/logout/', 
         auth_views.LogoutView.as_view(), 
         name='logout'),
    path('accounts/register/', 
         views.register, 
         name='register'),
    
    # Task management URLs
    path('create_project/', 
         views.create_project, 
         name='create_project'),
]