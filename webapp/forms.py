from django import forms
from django.core.exceptions import ValidationError
from django.forms import CheckboxSelectMultiple

from webapp.models import Type
from webapp.models import Issue
import string


def eng_letters_validator(summary):
    # проверяем требование на отсутствие кириллицы в поле 'summary'
    if not all(abc in string.printable for abc in summary):
        raise ValidationError(
            "You need to fill in only English letters"
        )
    return summary


def checkbox_qty_validator(type):
    # проверяем требование на кол-во выбранных типов задачи(проблемы) не более двух
    for i in type:
        if len(type) > 2:
            raise ValidationError(
                "You need to choose maximum two of types"
            )
    return type


class IssueForm(forms.ModelForm):
    summary = forms.CharField(
        max_length=200,
        required=True,
        label="Заголовок",
        validators=(eng_letters_validator,),
    )
    type = forms.ModelMultipleChoiceField(
        queryset=Type.objects.all(),
        widget=CheckboxSelectMultiple,
        validators=(checkbox_qty_validator,),
    )

    class Meta:
        model = Issue
        fields = (
            "summary",
            "description",
            "type",
            "status",
        )

        labels = {
            "summary": "Заголовок",
            "description": "Описание",
            "type": "Тип",
            "status": "Статус",
        }

    def clean_summary(self):
        summary = self.cleaned_data["summary"]
        if len(summary) < 2:
            raise ValidationError(
                "This field should be at least %(length)d symbols long!",
                code="too_short",
                params={"length": 2},
            )

        return summary
