from django.urls import path

from webapp.views.base import IndexView, IndexRedirectView
from webapp.views.issues import (
    IssueAdd,
    IssueDelete,
    ConfirmIssueDelete,
    IssueUpdate,
    IssueDetail,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "issue/",
        IndexRedirectView.as_view(),
        name="issue_index_redirect",
    ),
    path("issue/add", IssueAdd.as_view(), name="issue_add"),
    path(
        "issue/<int:pk>",
        IssueDetail.as_view(),
        name="issue_detail",
    ),
    path(
        "issue/<int:pk>/delete/",
        IssueDelete.as_view(),
        name="issue_delete",
    ),
    path(
        "issue/<int:pk>/confirm_delete/",
        ConfirmIssueDelete.as_view(),
        name="confirm_delete",
    ),
    path(
        "issue/<int:pk>/update/",
        IssueUpdate.as_view(),
        name="issue_update",
    ),
]
