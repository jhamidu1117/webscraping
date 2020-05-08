from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from landing.forms import SignUpForm, CreateProfileForm

# Create your views here.


def landing(request):
    return render(request, 'landing/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            prof = form.save()
            return redirect('home')
    else:
        form = CreateProfileForm(instance=request.user.profile)
    return render(request, 'signup.html', {'form': form})

