import unidecode
from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib.auth import get_user_model

from marketplace.utils import custom_file_name


class Category(models.Model):
    name = models.CharField(
        verbose_name="Назва",
        max_length=50
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        db_index=True,
        blank=True,
        verbose_name="URL",
    )
    description = models.TextField(
        verbose_name="Опис категорії",
          blank=True,
          null=True
        )

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse_lazy(
            "marketplace:category_detail", kwargs={"category_slug": self.slug}
        )

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(unidecode.unidecode(self.name))
        return super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Назва")
    description = models.TextField(verbose_name="Опис")
    price = models.DecimalField(
        max_digits=10,
          decimal_places=2,
          verbose_name="Ціна",
          null=True,
          blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    seller = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Продавець",
    )
    image = models.ImageField(
        upload_to=custom_file_name,
        null=True,
        blank=True,
        verbose_name="Фото",
    )
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата створення оголошення"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Змінено",
    )

    class Meta:
        verbose_name = "Оголошення"
        verbose_name_plural = "Оголошення"

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("marketplace:post_detail", kwargs={"pk": self.pk})


class Message(models.Model):
    sender = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="sent_messages",
    )
    receiver = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="received_messages",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="messages",
        blank=True,
        null=True,
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
