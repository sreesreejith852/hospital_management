from django.urls import path
from .views import RegisterAPI, LoginAPI, TaskCreateAPI, TaskListAPI


urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='api_register'),
    path('login/', LoginAPI.as_view(), name='api_login'),
    path('tasks/', TaskCreateAPI.as_view(), name='api_add_task'),
    path('tasks/all/', TaskListAPI.as_view(), name='api_view_tasks'),
]