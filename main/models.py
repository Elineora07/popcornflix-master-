from django.db import models
from django.utils.translation import gettext_lazy as _
from web.mixins import TranslateMixin


class Post(TranslateMixin, models.Model):
    translate_attributes = ['subject', 'content']

    subject_uz = models.CharField(max_length=100, verbose_name=_("Sarlavha (uz)"))
    subject_ru = models.CharField(max_length=100, verbose_name=_("Sarlavha (ru)"))
    content_uz = models.TextField(verbose_name=_("Content (uz)"))
    content_ru = models.TextField(verbose_name=_("Content (ru)"))
    image = models.ImageField()
    read = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
