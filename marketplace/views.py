from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from marketplace.models import Category


class HomePage(TemplateView):
    template_name = "marketplace/index.html"
    extra_context = {
        "title": "Головна сторінка",
        "cats": Category.objects.all(),
    }


# def index(request) -> HttpResponse:
#     context ={"title": "Головна сторінка"}
#     return render(
#         request,
#         "marketplace/index.html",
#         context,
#     )


def about(request) -> HttpResponse:
    return HttpResponse("<h1>Сторінка про сайт</h1>")


def contact(request) -> HttpResponse:
    return HttpResponse("<h1>Контакти</h1>")
