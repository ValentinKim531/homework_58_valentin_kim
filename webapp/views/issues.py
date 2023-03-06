from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.views.generic import TemplateView
from webapp.forms import IssueForm
from webapp.models import Issue


class IssueAdd(TemplateView):
    template_name = "issue_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = IssueForm()
        return context

    def post(self, request, *args, **kwargs):
        form = IssueForm(request.POST)
        if not form.is_valid():
            return render(
                request,
                "issue_create.html",
                context={"form": form},
            )

        else:
            issue = form.save()
            return redirect("issue_detail", pk=issue.pk)


class IssueUpdate(TemplateView):
    template_name = "issue_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["issue"] = get_object_or_404(
            Issue, pk=kwargs["pk"]
        )
        context["form"] = IssueForm(
            instance=context["issue"]
        )
        return context

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs["pk"])
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect("issue_detail", pk=issue.pk)
        return render(
            request, context={"form": form, "issue": issue}
        )


class IssueDetail(TemplateView):
    template_name = "issue_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["issue"] = get_object_or_404(
            Issue, pk=kwargs["pk"]
        )
        return context


class IssueDelete(TemplateView):
    template_name = "issue_confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["issue"] = get_object_or_404(
            Issue, pk=kwargs["pk"]
        )
        return context


class ConfirmIssueDelete(TemplateView):
    template_name = "index.html"

    def post(self, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs["pk"])
        issue.delete()
        return redirect("index")
