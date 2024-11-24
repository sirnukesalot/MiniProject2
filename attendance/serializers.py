from rest_framework import serializers
from courses.serializers import CourseSerializer
from students.serializers import StudentSerializer
from .models import Attendance
class AttendanceSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    course = CourseSerializer()

    class Meta:
        model = Attendance
        fields = ('id', 'student', 'course', 'date', 'status')