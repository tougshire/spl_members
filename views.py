from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django_filters_stoex.views import FilterView
from spl_members.forms import DepartmentForm, JobpositionForm, MemberForm
from spl_members.models import Department, Jobposition, Member

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from touglates.views import make_labels

class MemberCreate(PermissionRequiredMixin,CreateView):
    permission_required = "spl_members.add_member"
    template_name = 'spl_members/member_create.html'

    model = Member
    form_class = MemberForm

class MemberUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = "spl_members.change_member"
    template_name = 'spl_members/member_update.html'

    model = Member
    form_class = MemberForm

class MemberDetail(PermissionRequiredMixin, DetailView):
    permission_required = "spl_members.view_member"

    model = Member

    def get_context_data(self, **kwargs):
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

class MemberList(PermissionRequiredMixin,FilterView):
    permission_required = "spl_members.view_member"

    model = Member
    template_name = "spl_members/member_list.html"

    def get_context_data(self, *args, **kwargs):

        context_data = super().get_context_data(**kwargs)

        context_data["member_labels"] = make_labels(Member)

        return context_data

class DepartmentCreate(PermissionRequiredMixin,CreateView):
    permission_required = "spl_members.add_department"
    template_name = 'spl_members/department_create.html'

    model = Department
    form_class = DepartmentForm

class DepartmentUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = "spl_members.change_department"
    template_name = 'spl_members/department_update.html'

    model = Department
    form_class = DepartmentForm

class DepartmentDetail(PermissionRequiredMixin, DetailView):
    permission_required = "spl_members.view_department"

    model = Department

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data["department_labels"] = make_labels(Department)

        return context_data

class DepartmentDelete(PermissionRequiredMixin, DeleteView):
    permission_required = "spl_members.delete_department"
    model = Department
    success_url = reverse_lazy("spl_members:department-list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data["department_labels"] = make_labels(Department)

        return context_data

class DepartmentList(PermissionRequiredMixin,FilterView):
    permission_required = "spl_members.view_department"

    model = Department
    template_name = "spl_members/department_list.html"

    def get_context_data(self, *args, **kwargs):

        context_data = super().get_context_data(**kwargs)

        context_data["department_labels"] = make_labels(Department)

        return context_data

class JobpositionCreate(PermissionRequiredMixin,CreateView):
    permission_required = "spl_members.add_jobposition"
    model = Jobposition
    template_name = 'spl_members/jobposition_create.html'
    form_class = JobpositionForm

class JobpositionUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = "spl_members.change_jobposition"
    template_name = 'spl_members/jobposition_update.html'

    model = Jobposition
    form_class = JobpositionForm

class JobpositionDetail(PermissionRequiredMixin, DetailView):
    permission_required = "spl_members.view_jobposition"

    model = Jobposition

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data["jobposition_labels"] = make_labels(Jobposition)

        return context_data

class JobpositionDelete(PermissionRequiredMixin, DeleteView):
    permission_required = "spl_members.delete_jobposition"
    model = Jobposition
    success_url = reverse_lazy("spl_members:jobposition-list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data["jobposition_labels"] = make_labels(Jobposition)

        return context_data

class JobpositionList(PermissionRequiredMixin,FilterView):
    permission_required = "spl_members.view_jobposition"

    model = Jobposition
    template_name = "spl_members/jobposition_list.html"

    def get_context_data(self, *args, **kwargs):

        context_data = super().get_context_data(**kwargs)

        context_data["jobposition_labels"] = make_labels(Jobposition)

        return context_data
