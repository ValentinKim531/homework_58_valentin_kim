from django.db import models


class Status(models.Model):
    name = models.CharField(
        max_length=30, verbose_name="Статус"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"
