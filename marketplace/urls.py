from django.urls import path

from marketplace.views import HomePage, about, contact


app_name = "marketplace"

urlpatterns = [
    path("", HomePage.as_view(), name="index"),
    path("about/", about, name="index"),
    path("contact/", contact, name="index"),
]
