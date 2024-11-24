from celery import shared_task
from django.core.mail import send_mail
from students.models import Student

@shared_task
def attendance_reminder():

    students = Student.objects.all()
    for student in students:
        send_mail(
            'Mark your attendance',
            'Mark the attendance',
            'from@example.com',
            [student.email],
            fail_silently=False,
        )

@shared_task
def grade_notification(student_id, course_id, new_grade):
    student = Student.objects.get(id=student_id)
    send_mail(
        'New grade',
        f'New grade for {course_id} is {new_grade}.',
        'from@example.com',
        [student.email],
        fail_silently=False,
    )
