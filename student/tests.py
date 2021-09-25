from student.views import register_student
from django.test import TestCase
from .models import Student
import datetime
from django.urls import reverse
# Create your tests here.


class StudentModelTestCase(TestCase):
    def setUp(self) :
        self.student=Student(
        first_name="Mercy" ,
        last_name="Birungi",age=20,
        email="mercy@gmail.com",
        phone_number="0739049808",
        nationality="Ugandan",
        course_name="kotlin",
        gender="female",
        date_of_birth="2000"
        )
    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name,self.student.full_name())
    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name,self.student.full_name())
    def test_year_of_birth(self):
        current_year=datetime.datetime.now().year
        year=current_year-self.student.age
        self.assertEqual(year,self.student.year_of_birth)
    def test_student_registration_view(self):
        url=register_student
        data={"first_name": self.student.first_name,
            "last_name" :self.student.last_name,
            "email":self.student.email_address,
            "phone_number":self.student.phone_number,
            "nationanility":self.student.nationality,
            "course_name":self.student.course_name,
            "gender":self.student.gender,
            "date_of_birth":self.student.date_of_birth}
        request=self.client.past(url,data)
        self.assertEqual(request.status_code,200)


        

