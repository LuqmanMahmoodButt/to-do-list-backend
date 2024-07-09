from django.urls import path
from .views import TodolistView
 
urlpatterns = [
  path('', TodolistView.as_view()),
]