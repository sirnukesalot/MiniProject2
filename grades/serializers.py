from rest_framework import serializers
from courses.serializers import CourseSerializer
from students.serializers import StudentSerializer
from .models import Grade
from students.models import Student
from courses.models import Course
from users.models import User

class GradeSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    course = CourseSerializer()
    teacher = serializers.StringRelatedField()

    class Meta:
        model = Grade
        fields = ('id', 'student', 'course', 'grade', 'date', 'teacher')