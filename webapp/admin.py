from django.contrib import admin

from .models import Issue, Status, Type


# Register your models here.


class IssueAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "summary",
        "description",
        "status",
        "get_type",
    )
    list_filter = ("id", "summary", "description")
    search_fields = ("summary", "description")
    fields = ("summary", "description", "status", "type")
    readonly_fields = ("id", "created_at", "updated_at")

    def get_type(self, instance):
        return [type.name for type in instance.type.all()]


admin.site.register(Issue, IssueAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_filter = ("id", "name")
    search_fields = ("name",)
    fields = ("name",)
    readonly_fields = ("id", "created_at")


admin.site.register(Type, TypeAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_filter = ("id", "name")
    search_fields = ("name",)
    fields = ("name",)
    readonly_fields = ("id", "created_at")


admin.site.register(Status, StatusAdmin)
