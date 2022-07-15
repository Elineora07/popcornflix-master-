from django.urls import path
from .views import account_registration

app_name = "account"

urlpatterns = [
    path('account/registration/', account_registration, name="registration")
]
