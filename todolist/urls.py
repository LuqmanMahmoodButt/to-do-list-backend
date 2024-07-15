from django.urls import path
from .views import TodolistView, TodolistDetailView
 
urlpatterns = [
  path('', TodolistView.as_view()),
  path('<int:pk>/', TodolistDetailView.as_view(), name='itemlist-detail'),

]