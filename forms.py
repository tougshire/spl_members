from django import forms
from django.forms import inlineformset_factory
from django.urls import reverse_lazy

from touglates.widgets import TouglatesRelatedSelect
from .models import Attachmenttype, Department, Jobposition, Member

class JobpositionSelect(TouglatesRelatedSelect):
    def create_option(
        self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        created_option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            if value.instance.department:
                created_option['label'] = created_option['label'] + ' ' + str(value.instance.department.abbreviation)
        return created_option

class CSVOptionForm(forms.Form):

    make_csv = forms.BooleanField(
        label="CSV",
        initial=False,
        required=False,
        help_text="Download the result as a CSV file",
    )


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = [
            "name",
            "abbreviation",
            "container",
        ]


class JobpositionForm(forms.ModelForm):
    class Meta:
        model = Jobposition
        fields = [
            "title",
            "grade",
            "department",
            "supervisor",
        ]
        widgets = {
            "department": TouglatesRelatedSelect(
                related_data={
                    "model_name": "Department",
                    "app_name": "spl_members",
                    "add_url": reverse_lazy("spl_members:department-popup"),
                },
                add_filter_input=True,
            ),
        }


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            "name_prefered",
            "surname",
            "name_full",
            "jobposition",
            "email",
            "phone",
            "start_date",
            "end_date",
        ]
        widgets = {
            "jobposition": TouglatesRelatedSelect(
                related_data={
                    "model_name": "Jobposition",
                    "app_name": "spl_members",
                    "add_url": reverse_lazy("spl_members:jobposition-popup"),
                },
                add_filter_input=True,
            ),
        }
