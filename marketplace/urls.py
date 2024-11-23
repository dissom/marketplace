from django.urls import path

from marketplace.views import CategoryDetailView, HomePage, PostCreateView, PostDetailView, about, contact


app_name = "marketplace"

urlpatterns = [
    path("", HomePage.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/create/", PostCreateView.as_view(), name="post_create"),
    path("category/<slug:category_slug>/", CategoryDetailView.as_view(), name="category_detail"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
]
