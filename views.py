from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from django_filters_stoex.views import FilterView
from spl_members.forms import MemberForm
from spl_members.models import Member


class MemberCreate(CreateView):
    model = Member
    form_class = MemberForm


class MemberUpdate(UpdateView):
    model = Member
    form_class = MemberForm


class MemberDetail(DetailView):
    model = Member


class MemberList(FilterView):
    model = Member
    template_name = "spl_members/member_list.html"
