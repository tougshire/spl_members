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
        "member/list/",
        views.MemberList.as_view(),
        name="member-list",
    ),
    path(
        "member/<int:pk>/detail/",
        views.MemberDetail.as_view(),
        name="member-detail",
    ),
]
