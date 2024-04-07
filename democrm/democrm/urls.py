from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from core.views import index, about
from userprof.views import signup

urlpatterns = [
    path('', index, name ='index'),
    path('about/', about, name ='about'),
    path('dashboard/', include('dashboard.urls')),
    path('sign-up/', signup, name ='signup'),
    path('log-in/', views.LoginView.as_view(template_name='userprof/login.html'), name='login'),
    path('log-out/', views.LoginView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]