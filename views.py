from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django_filters_stoex.views import FilterView
from spl_members.forms import MemberForm
from spl_members.models import Member

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from touglates.views import make_labels

class MemberCreate(CreateView):
    model = Member
    form_class = MemberForm


class MemberUpdate(UpdateView):
    model = Member
    form_class = MemberForm


class MemberDetail(PermissionRequiredMixin, DetailView):
    permission_required = "spl_members.view_member"

    model = Member

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data["member_labels"] = make_labels(Member)

        return context_data


class MemberList(FilterView):
    model = Member
    template_name = "spl_members/member_list.html"

    def get_context_data(self, *args, **kwargs):

        context_data = super().get_context_data(**kwargs)

        context_data["member_labels"] = make_labels(Member)

        return context_data

class MemberDelete(PermissionRequiredMixin, DeleteView):
    permission_required = "spl_members.delete_member"
    model = Member
    success_url = reverse_lazy("spl_members:member-list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data["member_labels"] = make_labels(Member)

        return context_data
