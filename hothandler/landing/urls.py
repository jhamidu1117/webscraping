from django.urls import path, include, reverse
from landing import views

urlpatterns = [
    path('', views.landing, name='home'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile')
]
