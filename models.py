from datetime import date
from django.db import models
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(
        "name",
        max_length=50,
        help_text="The name of the department",
    )
    abbreviation = models.CharField(
        "abbreviation",
        blank=True,
        max_length=10,
        help_text="An abbrevation, or code, for the department",
    )
    container = models.ForeignKey(
        "Department",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="The departemnt of which this department is part",
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Jobposition(models.Model):
    title = models.CharField(
        "title",
        max_length=50,
        help_text="The title to be used before the person's name",
    )
    grade = models.CharField(
        "Grade",
        max_length=10,
        blank=True,
        help_text="For alphabetical ordering.  An indication of the position within a hierarchy",
    )
    department = models.ForeignKey(
        Department,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="The position's department",
    )
    supervisor = models.ForeignKey(
        "Jobposition",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="The positions's supervisor",
    )
    email = models.EmailField(
        "email", blank=True, help_text="The job position's email address."
    )
    phone = models.CharField(
        "phone", max_length=30, blank=True, help_text="The job positions's phone number"
    )
    def __str__(self):
        return self.title

    class Meta:
        ordering = [
            "-grade",
            "department",
        ]


class Attachmenttype(models.Model):
    name = models.CharField(
        "name",
        max_length=50,
        help_text="The name of the type of attachment",
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Member(models.Model):

    name_prefered = models.CharField(
        "prefered name",
        max_length=20,
        help_text="The person's first name or prefered name to be used it's place",
    )
    surname = models.CharField(
        "surname",
        max_length=60,
        help_text="The person's surname name, or acceptable alternative",
    )
    name_full = models.CharField(
        "full name",
        max_length=80,
        help_text="The full name of the member, the format of which should be consistantly applied throughout",
    )
    jobposition = models.ForeignKey(
        Jobposition,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="The person's job position in the organization",
        verbose_name="Job Position"
    )
    email = models.EmailField(
        "email", blank=True, help_text="The members's email address"
    )
    phone = models.CharField(
        "phone", max_length=30, blank=True, help_text="The member's phone number"
    )
    start_date = models.DateField(
        blank=True,
        null=True,
        help_text="The date this person became part of this organiztion.  Automatically updated by status of is_active",
    )
    end_date = models.DateField(
        blank=True,
        null=True,
        help_text="The date this person detached from this organization.  Automatically updated by status of is_active",
    )
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text="If the person is currently attached to the organization.",
    )
    is_individual = models.BooleanField(
        "is an individual",
        default=True,
        help_text="Is this member an individual (as opposed to an organization or other entity which might be viewed as an individual for purposes of this data)",
    )

    def get_absolute_url(self):
        return reverse("spl_members:member-detail", kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self.is_active:
            if self.start_date is None:
                self.start_date = date.today()
            if self.end_date is not None and self.end_date >= self.start_date:
                self.end_date = None
        else:  # not active
            if self.end_date is None:
                self.end_date = date.today()
            if self.start_date is not None and self.start_date >= self.end_date:
                self.start_date = None

        super().save(*args, **kwargs)

    def get_supervisor(self):
        try:
            return self.jobposition.supervisor.member_set.first()
        except:
            try:
                return self.jobposition.supervisor
            except:
                return None

    def __str__(self):
        return self.name_full

    class Meta:
        ordering = (
            "is_active",
            "surname",
            "start_date",
        )
