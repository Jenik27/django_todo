from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<str:pk>/', views.deleteTask, name='delete'),
    path('update/<str:pk>/', views.updateTask, name='update'),
]