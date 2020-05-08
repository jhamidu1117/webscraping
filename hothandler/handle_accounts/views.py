from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from handle_accounts.models import Platform

# Create your views here.


@login_required
def dashboard(request):
    user = request.user
    accounts_to_handle = Platform.objects.filter(user_account=user)
    return render(request, 'handle_accounts/dashboard.html', {'accounts': accounts_to_handle})

