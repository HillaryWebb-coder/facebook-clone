from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.conf import settings
from .models import Profile


class UserEditForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email")


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ("date_of_birth", "photo")
