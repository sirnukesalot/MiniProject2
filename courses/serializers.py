from rest_framework import serializers
from students.serializers import StudentSerializer
from .models import Course, Enrollment


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'instructor']


class EnrollmentSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = Enrollment
        fields = ('id', 'student', 'course', 'date_enrolled')

def get_student_serializer():
    from students.serializers import StudentSerializer
    return StudentSerializer