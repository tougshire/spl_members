from datetime import date
from django.test import TestCase
from .models import Attachmenttype, Department, Jobposition, Member


class GeneralModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.employee = Attachmenttype.objects.create(name="Employee")
        cls.research_and_collections = Department.objects.create(
            name="Research and Collections"
        )
        cls.collection_development = Department.objects.create(
            name="Collection Development",
            container=Department.objects.get(name="Research and Collections"),
        )
        cls.information = Department.objects.create(name="Information Department")
        cls.technology_support = Department.objects.create(
            name="Technology Support", container=cls.information
        )
        cls.assistant_director = Jobposition.objects.create(
            title="Assistant Director", grade="9"
        )
        cls.director = Jobposition.objects.create(title="Director", grade="10")
        cls.research_librarian = Jobposition.objects.create(
            title="Research Librarian",
            grade="8",
            department=Department.objects.get(name="Research and Collections"),
        )
        cls.technology_officer = Jobposition.objects.create(
            title="Technology Officer", grade="8", department=cls.information
        )
        cls.technician = Jobposition.objects.create(
            title="Technician ", grade="7", department=cls.technology_support
        )
        cls.kim_bixby = Member.objects.create(
            name_full="Kim Bixby", jobposition=cls.technology_officer
        )
        cls.benjamin_tougshire = Member.objects.create(
            name_full="Benjamin Tougshire", jobposition=cls.technician
        )

    def test_model_has_str(self):
        self.assertEqual(self.employee.__str__(), "Employee")
        self.assertEqual(
            self.research_and_collections.__str__(), "Research and Collections"
        )
        self.assertEqual(
            list(self.research_and_collections.department_set.all()),
            [
                self.collection_development,
            ],
        )
        self.assertEqual(self.assistant_director.__str__(), "Assistant Director")
        self.assertEqual(
            self.research_librarian.__str__(),
            "Research Librarian Research and Collections",
        )
        self.assertEqual(self.kim_bixby.__str__(), "Kim Bixby")

    def test_active(self):
        self.assertEqual(self.benjamin_tougshire.start_date, date.today())
        self.assertIsNone(self.benjamin_tougshire.end_date)
        self.assertEqual(self.benjamin_tougshire.is_active, True)

        self.benjamin_tougshire.is_active = False
        self.benjamin_tougshire.save()
        self.assertIsNone(self.benjamin_tougshire.start_date)
        self.assertEqual(self.benjamin_tougshire.end_date, date.today())

        self.benjamin_tougshire.start_date = date(2000, 1, 1)
        self.benjamin_tougshire.save()

        self.benjamin_tougshire.is_active = True
        self.benjamin_tougshire.save()
        self.assertIsNone(self.benjamin_tougshire.end_date)
        self.assertEqual(self.benjamin_tougshire.start_date, date(2000, 1, 1))

    def test_ordering(self):
        pass
