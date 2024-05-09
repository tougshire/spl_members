from django import forms
from django.forms import inlineformset_factory
from .models import Attachmenttype, Department, Jobposition, Member


class CSVOptionForm(forms.Form):

    make_csv = forms.BooleanField(
        label="CSV",
        initial=False,
        required=False,
        help_text="Download the result as a CSV file",
    )


class AttachmenttypeForm(forms.Modelform):
    class Meta:
        model = Attachmenttype
        fields = ["_all_"]


class DepartmentForm(forms.Modelform):
    class Meta:
        model = Department
        fields = ["_all_"]


class JobpositionForm(forms.Modelform):
    class Meta:
        model = Jobposition
        fields = ["_all_"]


class MemberForm(forms.Modelform):
    class Meta:
        model = Member
        fields = [
            "name_preferred",
            "surname",
            "name_full",
            "job_position",
            "email",
            "phone",
            "start_date",
            "end_date",
        ]
