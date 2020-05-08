from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from handle_accounts.models import Platform
from handle_accounts.forms import SyncForm
from handle_accounts import cipher
from base64 import b64encode


# Create your views here.


@login_required
def dashboard(request):
    user = request.user
    accounts_to_handle = Platform.objects.filter(user_account=user)
    return render(request, 'handle_accounts/dashboard.html', {'accounts_to_handle': accounts_to_handle})


@login_required
def sync_accounts(request, pk):
    user = request.user
    if request.method == 'POST':
        platform = get_object_or_404(Platform, pk=pk, user_account=user)
        form = SyncForm(request.POST, instance=platform)
        if form.is_valid():
            platform = form.save(commit=False)
            account_key = cipher.true_key(user.profile.uname_id)
            account_iv = cipher.true_iv(user.profile.email_id)
            secret_name = cipher.true_encrypt(key=account_key, iv=account_iv, data=platform.platform_user_name)
            secret_password = cipher.true_encrypt(key=account_key, iv=account_iv, data=platform.platform_user_password)
            platform.platform_user_name = secret_name
            platform.platform_user_password = secret_password
            platform.save()
            return redirect('dashboard')
    else:
        platform = get_object_or_404(Platform, pk=pk, user_account=user)
        platform.platform_user_name = ''
        platform.platform_user_password = ''
        form = SyncForm(instance=platform)
        return render(request, 'handle_accounts/addAccount.html', {'form': form})


@login_required
def add_accounts(request):
    user = request.user
    if request.method == 'POST':
        platform = Platform(user_account=user)
        form = SyncForm(request.POST, instance=platform)
        if form.is_valid():
            platform = form.save(commit=False)
            account_key = cipher.true_key(user.profile.uname_id)
            account_iv = cipher.true_iv(user.profile.email_id)
            secret_name = cipher.true_encrypt(key=account_key, iv=account_iv, data=platform.platform_user_name)
            secret_password = cipher.true_encrypt(key=account_key, iv=account_iv, data=platform.platform_user_password)
            platform.platform_user_name = secret_name
            platform.platform_user_password = secret_password
            platform.save()
            return redirect('dashboard')
    else:
        platform = Platform(user_account=user)
        form = SyncForm(instance=platform)
        return render(request, 'handle_accounts/addAccount.html', {'form': form})
