from django.urls import path
from . import views

urlpatterns = [
    path('', views.assignment_list, name='assignment_list'),
    path('add/', views.assignment_create, name='assignment_add'),
    path('complete/<int:pk>/', views.assignment_complete, name='assignment_complete'),
    path('delete/<int:pk>/', views.assignment_delete, name='assignment_delete'),
]
