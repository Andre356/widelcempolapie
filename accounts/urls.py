from django.urls import path
from . import views as account_views


app_name = 'accounts'

urlpatterns = [
    path('signup/', account_views.signup, name='signup'),
    ]



