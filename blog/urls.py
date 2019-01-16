from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:dish_id>/', views.detail, name='detail'),
]
