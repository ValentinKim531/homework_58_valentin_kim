from django.db import models
from django.utils import timezone


class Issue(models.Model):
    summary = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Заголовок",
    )

    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        verbose_name="Описание",
    )
    type = models.ManyToManyField(
        to="webapp.Type",
        related_name="issues",
        verbose_name="Тип",
        blank=False,
    )
    status = models.ForeignKey(
        "webapp.Status",
        related_name="issues",
        verbose_name="Статус",
        on_delete=models.RESTRICT,
        blank=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления",
    )
    is_deleted = models.BooleanField(
        verbose_name="удалено", null=False, default=False
    )
    deleted_at = models.DateTimeField(
        verbose_name="Дата и время удаления",
        null=True,
        default=None,
    )

    def __str__(self):
        return f"{self.summary} - {self.description} - {self.status} - {self.type}"

    class Meta:
        verbose_name = "Проблема"
        verbose_name_plural = "Проблемы"
        ordering = ["-created_at"]

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
