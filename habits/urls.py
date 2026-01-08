from django.urls import path
from . import views

urlpatterns = [
    path('', views.habit_list, name='habit_list'),
    path('add/', views.habit_create, name='habit_add'),
    path('done/<int:pk>/', views.habit_done, name='habit_done'),
    path('delete/<int:pk>/', views.habit_delete, name='habit_delete'),
]
