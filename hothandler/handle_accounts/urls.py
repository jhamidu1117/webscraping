from django.urls import path, include, reverse
from handle_accounts import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]
