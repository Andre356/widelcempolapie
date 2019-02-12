from django.urls import path
from .views import HomePageView, DetailDishView, CreateDishView, UpdateDishView, DeleteDishView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<int:pk>/', DetailDishView.as_view(), name='detail'),
    path('create/', CreateDishView.as_view(), name='dish-create'),
    path('update/<int:pk>/', UpdateDishView.as_view(), name='dish-update'),
    path('delete/<int:pk>/', DeleteDishView.as_view(), name='dish-delete'),
]
