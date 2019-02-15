from django.urls import path
from .views import HomePageView, DetailDishView, CreateDishView, UpdateDishView, DeleteDishView
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<int:pk>/', DetailDishView.as_view(), name='detail'),
    path('create/', staff_member_required(CreateDishView.as_view()), name='dish-create'),
    path('update/<int:pk>/', staff_member_required(UpdateDishView.as_view()), name='dish-update'),
    path('delete/<int:pk>/', staff_member_required(DeleteDishView.as_view()), name='dish-delete'),
]
