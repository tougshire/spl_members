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


class AttachmenttypeForm(forms.ModelForm):
    class Meta:
        model = Attachmenttype
        fields = "__all__"


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
