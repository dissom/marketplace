from django.contrib import admin
from django.utils.safestring import mark_safe

from marketplace.models import Category, Post, Message


admin.site.register(Message)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "category",
        "description",
        "seller",
        "post_image",
        "image",
    )
    readonly_fields = ("post_image",)
    list_display = (
        "id",
        "title",
        "category",
        "description",
        "seller",
        "post_image",
        "created_at",
        "updated_at",
    )

    @admin.display(description="Фото", ordering="content")
    def post_image(self, post: Post) -> str:

        """Додаємо кастомну колонку"""
        if post.image:
            return mark_safe(f"<img src='{post.image.url}' width=100>")
        return "Брак фото"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "description",)
    list_display_links = ("id", "name")
