from rest_framework import viewsets
from .models import Grade
from .serializers import GradeSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsTeacher, IsAdmin
import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAuthenticated(), IsTeacher()]
        return [IsAuthenticated(), IsAdmin()]

logger = logging.getLogger('django')

class UpdateGradeView(APIView):
    def post(self, request, *args, **kwargs):
        student = request.data.get('student')
        course_id = request.data.get('course_id')
        grade = request.data.get('grade')
        grade_record, created = Grade.objects.update_or_create(student_id=student, course_id=course_id,defaults={'grade': grade})
        action = 'Created' if created else 'Updated'
        logger.info(f'{action} grade for student {student} in course {course_id} with grade {grade}')
        return Response({"message": "Grade updated successfully"}, status=200)