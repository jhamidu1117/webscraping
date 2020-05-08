from django.urls import path, include, reverse
from handle_accounts import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_account', views.add_accounts, name='add'),
    path('link_accounts/<int:pk>', views.sync_accounts, name='sync')
]
