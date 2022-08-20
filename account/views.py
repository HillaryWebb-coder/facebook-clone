from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Custom Imports
from .forms import UserEditForm, ProfileEditForm
from .models import Profile
# Create your views here.


def registerView(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save()
        Profile.objects.create(user=new_user)
        return redirect(reverse("login"))
    return render(request, "account/register.html", {"form": form})


@login_required
def dashboardView(request):
    return render(request, "account/dashboard.html", {'section': 'dashboard'})


@login_required
def editProfileView(request):
    user_form = UserEditForm(instance=request.user, data=request.POST or None)
    profile_form = ProfileEditForm(
        instance=request.user.profile, data=request.POST or None, files=request.FILES)

    if user_form.is_valid() and profile_form.is_valid():
        profile_form.save()
        user_form.save()
        messages.success(request, "profile updated successfully")
    return render(request, "account/edit.html", {"user_form": user_form, "profile_form": profile_form})
