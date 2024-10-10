from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='notes'),
    path('add/', views.add, name='add'),
    path('note/<int:pk>/', views.detail, name='detail'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('edit/<int:pk>/', views.edit, name='edit'),
]
