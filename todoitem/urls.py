from django.urls import path
from .views import ItemlistView, itemlistDetailView


urlpatterns = [
    path('todoitems/', ItemlistView.as_view(), name='itemlist'),
    path('todoitems/<int:pk>/', itemlistDetailView.as_view(), name='itemlist-detail'),
]