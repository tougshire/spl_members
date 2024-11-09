from django.views.generic.base import RedirectView
from django.urls import path, reverse_lazy
from . import views

app_name = "spl_members"

urlpatterns = [
    path("", RedirectView.as_view(url=reverse_lazy("spl_members:member-list"))),
    path(
        "member/create/",
        views.MemberCreate.as_view(),
        name="member-create",
    ),
    path(
        "member/update/<int:pk>/",
        views.MemberUpdate.as_view(),
        name="member-update",
    ),
    path(
        "member/<int:pk>/detail/",
        views.MemberDetail.as_view(),
        name="member-detail",
    ),
    path(
        "member/<int:pk>/delete/",
        views.MemberDelete.as_view(),
        name="member-delete",
    ),
    path(
        "member/list/",
        views.MemberList.as_view(),
        name="member-list",
    ),
    path(
        "department/create/",
        views.DepartmentCreate.as_view(),
        name="department-create",
    ),
    path(
        "department/popup/",
        views.DepartmentCreate.as_view(),
        name="department-popup",
        kwargs={'popup':True}
    ),
    path(
        "department/update/<int:pk>/",
        views.DepartmentUpdate.as_view(),
        name="department-update",
    ),
    path(
        "department/<int:pk>/detail/",
        views.DepartmentDetail.as_view(),
        name="department-detail",
    ),
    path(
        "department/<int:pk>/delete/",
        views.DepartmentDelete.as_view(),
        name="department-delete",
    ),
    path(
        "department/list/",
        views.DepartmentList.as_view(),
        name="department-list",
    ),
    path(
        "jobposition/create/",
        views.JobpositionCreate.as_view(),
        name="jobposition-create",
    ),
    path(
        "jobposition/popup/",
        views.JobpositionCreate.as_view(),
        name="jobposition-popup",
        kwargs={'popup': True},

    ),
    path(
        "jobposition/update/<int:pk>/",
        views.JobpositionUpdate.as_view(),
        name="jobposition-update",
    ),
    path(
        "jobposition/<int:pk>/detail/",
        views.JobpositionDetail.as_view(),
        name="jobposition-detail",
    ),
    path(
        "jobposition/<int:pk>/delete/",
        views.JobpositionDelete.as_view(),
        name="jobposition-delete",
    ),
    path(
        "jobposition/list/",
        views.JobpositionList.as_view(),
        name="jobposition-list",
    ),

]
