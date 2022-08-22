from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Custom Imports
from .forms import UserEditForm, ProfileEditForm
from .models import Profile


def registerView(request):
    """
    Allow the users to register and create a new account
    """
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save()
        return redirect(reverse("login"))
    return render(request, "account/register.html", {"form": form})


@login_required
def dashboardView(request):
    """
    Display the user dashboard
    """
    return render(request, "account/dashboard.html", {'section': 'dashboard'})


@login_required
def editProfileView(request):
    """
    Users can edit their profile from their dashboard
    """
    user_form = UserEditForm(instance=request.user, data=request.POST or None)
    profile_form = ProfileEditForm(
        instance=request.user.profile, data=request.POST or None, files=request.FILES)

    if user_form.is_valid() and profile_form.is_valid():
        profile_form.save()
        user_form.save()
        messages.success(request, "profile updated successfully")
    return render(request, "account/edit.html", {"user_form": user_form, "profile_form": profile_form})
