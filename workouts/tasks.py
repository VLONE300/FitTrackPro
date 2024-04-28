from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from workouts.models import TrainingProgram


@shared_task
def send_create_program_mail(user_email):
    send_mail(f'Ваша прогрмма тренировок готова',
              'Мы будем присылать напоминания о предстоящих тренировках',
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=[user_email],
              )


@shared_task
def training_reminder():
    programs = TrainingProgram.objects.all()
    for program in programs:
        user_email = program.user.email
        send_mail(f'Напоминание о вашей тренировке {program.name}',
                  'Не забудьте подготовиться к вашей тренировке!',
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[user_email],)


