from django.urls import path
from . import views
from .views import HomePageView, DetailDishView

urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomePageView.as_view(), name='home'),
    #path('<int:dish_id>/', views.detail, name='detail'),
    path('<int:pk>/', DetailDishView.as_view(), name='detail'),
]
