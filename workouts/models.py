from django.db import models

from users.models import CustomUser


class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class TrainingExercise(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.exercise.name} - {self.sets} sets - {self.reps} reps'


class TrainingProgram(models.Model):
    TRAINING_TYPE = (
        ('Personal', 'Personal'),
        ('General ', 'General ')
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    training_type = models.CharField(max_length=10, choices=TRAINING_TYPE)
    exercises = models.ManyToManyField(TrainingExercise)

    def __str__(self):
        return self.name


class ExerciseResult(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='exercise_results')
    training_exercise = models.ForeignKey(TrainingExercise, on_delete=models.CASCADE)
    date = models.DateField()
    sets_completed = models.PositiveIntegerField()
    reps_completed = models.PositiveIntegerField()
    weight_lifted = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.training_exercise.exercise} - {self.date}'
