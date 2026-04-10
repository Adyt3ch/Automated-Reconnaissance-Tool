from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('scan/new/', views.new_scan, name='new_scan'),
    path('scan/<int:pk>/', views.scan_detail, name='scan_detail'),
]