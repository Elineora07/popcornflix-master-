from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import RegistrationForm
from django.utils.translation import gettext_lazy as _


def account_registration(request):
    page_title = _("Ro'yhatdan o'tish")
    request.button_title = page_title
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('main:index')

    return render(request, "account/registration.html", {

        'form': form
    })


# Create your views here.
