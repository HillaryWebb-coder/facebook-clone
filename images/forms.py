from dataclasses import fields
from django import forms

# Custom imports
from .models import Image


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ("user", "title", "image", "description")
        widgets = {
            "user": forms.HiddenInput,
        }
