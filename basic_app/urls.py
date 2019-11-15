from django.urls import path
from basic_app import views

app_name = 'basic_app'

url_patterns = [
    path('register/', views.register, name='register'),
]