from django import forms
from django.contrib.auth.models import User
from handle_accounts.models import Platform


class SyncForm(forms.ModelForm):
    platform_user_name = forms.CharField(max_length=254, required=True, widget=forms.TextInput())
    platform_user_password = forms.CharField(max_length=254, required=True, widget=forms.PasswordInput())

    class Meta:
        model = Platform
        fields = ('platform_name', 'platform_user_name', 'platform_user_password')


class PassForm(forms.Form):
    pass_phrase = forms.CharField(max_length=254, required=True, widget=forms.TextInput())
