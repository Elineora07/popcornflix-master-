from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["subject_uz", 'content_uz', 'subject_ru', 'content_ru', 'image']
