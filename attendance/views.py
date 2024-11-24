from rest_framework import viewsets
from .models import Attendance
from .serializers import AttendanceSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsTeacher, IsAdmin
import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



class MarkAttendanceView(APIView):

    def post(self, request, *args, **kwargs):
        student = request.user
        course_id = request.data.get('course_id')
        status = request.data.get('status')

        attendance, created = Attendance.objects.update_or_create(
            student=student, course_id=course_id,
            defaults={'status': status}
        )
        action = 'Created' if created else 'Updated'
        logger.info(f'{action} attendance for {student.email} in course {course_id} with status {status}')
        return Response({"message": "Attendance marked successfully"}, status=200)


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAuthenticated(), IsTeacher()]
        return [IsAuthenticated(), IsAdmin()]

logger = logging.getLogger('django')