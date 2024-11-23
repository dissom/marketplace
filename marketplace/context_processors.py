from django.db.models import Count

from marketplace.models import Category


def categories_context(request):
    return {
        "cats": Category.objects.annotate(
            post_count=Count("posts"))
            .filter(post_count__gt=0)
    }
