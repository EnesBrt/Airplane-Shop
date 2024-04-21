from django.urls import include, path
from .views import ActivateAccountView

urlpatterns = [
    path(
        "activate/<uidb64>/<token>/",
        ActivateAccountView.as_view(),
        name="activate_account",
    ),
]
