from django.urls import path
from . import views

urlpatterns = [
    path('create/',
    views.create,
    name='create'
    ),
    path('list/',views.list,name='list'),
    path('edit/<pk>',views.edit,name = 'edit'),
    path('delete/<pk>',views.delete,name ='delete'),
    # path('',views.edit,name = 'edit'),
    
]