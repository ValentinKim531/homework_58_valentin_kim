from django.db import models


class Type(models.Model):
    name = models.CharField(
        max_length=30, verbose_name="Тип"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"
