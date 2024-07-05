from django.urls import path
from .views import TodoItemViewSet, CarDetailView
 
urlpatterns = [
  path('', TodoItemViewSet.as_view()),
]