from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, ListView

from marketplace.models import Category, Post


class HomePage(TemplateView):
    template_name = "marketplace/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Головна сторінка"
        context["posts"] = Post.objects.order_by("-created_at")
        return context


class CategoryDetailView(DetailView):
    template_name = "marketplace/category_detail.html"
    slug_url_kwarg = "category_slug"
    context_object_name = "category"

    def get_queryset(self) -> QuerySet[Any]:
        return Category.objects.all()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(category=self.object).order_by(
            "-created_at"
        )

        return context


class PostCreateView(CreateView):
    model = Post
    template_name = "marketplace/post_create.html"
    fields = "__all__"
    # form_class = PostCreationForm
    success_url = reverse_lazy("marketplace:index")


# class PostsListView(ListView):
#     model = Post
#     template_name = "marketplace/post_list.html"
#     context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "marketplace/post_detail.html"
    context_object_name = "post"
    extra_context = {"cats": Category.objects.all()}


def about(request) -> HttpResponse:
    return HttpResponse("<h1>Сторінка про сайт</h1>")


def contact(request) -> HttpResponse:
    return HttpResponse("<h1>Контакти</h1>")
