from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, verbose_name=_("User"), on_delete=models.CASCADE)
    date_of_birth = models.DateField(_("Date Of Birth"), blank=True, null=True)
    photo = models.ImageField(
        _("Avatar"), upload_to='users/%Y/%m/%d/', blank=True)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return f"Profile for user: {self.user.username}"
