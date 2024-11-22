from django.db import models
from django.contrib.auth import get_user_model

from marketplace.utils import custom_file_name


class Category(models.Model):
    name = models.CharField(
        verbose_name="Категорія",
        max_length=50
    )
    description = models.TextField(
        verbose_name="Опис категорії",
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
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
        related_name="category"
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
        auto_now_add=True,
        verbose_name="Дата створення оголошення"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Змінено",
    )

    def __str__(self) -> str:
        return self.name
