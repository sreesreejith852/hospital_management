from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_task/', views.add_task, name='add_task'),
    path('logout/', views.user_logout, name='logout'),
]