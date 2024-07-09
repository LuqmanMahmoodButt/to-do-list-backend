from django.urls import path
from .views import ItemlistView, itemlistDetailView


urlpatterns = [
    path('', ItemlistView.as_view(), name='itemlist'),
    path('<int:pk>/', itemlistDetailView.as_view(), name='itemlist-detail'),
]