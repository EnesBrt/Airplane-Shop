from django.urls import include, path
from . import views

urlpatterns = [
    path(
        "activate/<uidb64>/<token>/",
        ActivateAccountView.as_view(),
        name="activate_account",
    ),
]
