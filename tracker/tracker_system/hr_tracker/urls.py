from django.urls import path
from . import views

urlpatterns = (
    path('create_task/',views.create_task,name='create_task'),
    path('list_task/',views.list_task,name='list_task'),
    path('',views.create_task,name='create_task')

)