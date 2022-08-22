from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
# Create your models here.


class Image(models.Model):

    user = models.ForeignKey(get_user_model(), verbose_name=_(
        "User"), on_delete=models.CASCADE, related_name="images_created")
    title = models.CharField(_("Title"), max_length=200)
    slug = models.SlugField(_("Slug"), max_length=200, blank=True)
    image = models.ImageField(_("Image"), upload_to="images/%Y/%m/%d")
    description = models.TextField(_("Description"), blank=True)
    users_like = models.ManyToManyField(get_user_model(), verbose_name=_(
        "Users Likes"), blank=True, related_name="images_liked")
    created = models.DateField(
        _("Created at"), auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = _("image")
        verbose_name_plural = _("images")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Image, self).save(*args, **kwargs)
