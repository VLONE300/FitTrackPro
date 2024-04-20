from django.db import models

from users.models import CustomUser, Trainer
from workouts.models import TrainingProgram


class UserTrainingProgram(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='training_programs')
    program = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'Program {self.program} for user {self.user}'


class UserProgress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='progress')
    program = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f'Progress {self.user}'


# class UserTrainingProgram(models.Model):
#     trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='training_programs')
#     program = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     # Добавляем дополнительные поля для прогресса пользователя в рамках программы
#     weight = models.DecimalField(max_digits=5, decimal_places=2, default=0)
#     description = models.TextField(default="No progress yet")
#
#     def __str__(self):
#         return f'Program {self.program} for user {self.user}'