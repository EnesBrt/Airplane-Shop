from django.urls import include, path

urlpatterns = [
    path(
        "verify-email/<uidb64>/<token>/",
        VerifyEmailView.as_view(),
        name="customer:verify-email",
    ),
]
