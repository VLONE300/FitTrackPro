from django.core.mail import send_mail
from users.models import CustomUser
from celery import shared_task
from django.conf import settings


@shared_task
def send_create_program_email(user_email):
    send_mail('Тренировочная программа',
              'Вы успешно создали свою тренировочную программу, теперь мы будем присылать напоминания'
              'о ваших тренировках',
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=[user_email],
              fail_silently=False
              )
