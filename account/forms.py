from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    confirm = forms.CharField(label=_("Parol takroran"), widget=forms.PasswordInput)

    def clean_confirm(self):
        if self.cleaned_data['confirm'] != self.cleaned_data['password']:
            raise ValidationError

        return self.cleaned_data['confirm']

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email', 'password']
        labels = {
            'username': _("Login"),
            'last_name': _("Familiya"),
            'first_name': _("Ismingiz"),
            'email': _("E-mail"),
            'password': _("Parol")
        }

        widgets = {
            'password': forms.PasswordInput
        }