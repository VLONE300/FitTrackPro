from django.db import models


class TrainingProgram(models.Model):
    TRAINING_TYPE = (
        ('Personal', 'Personal'),
        ('General ', 'General ')
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    training_type = models.CharField(max_length=10, choices=TRAINING_TYPE)

    exercises = models.ManyToManyField('Exercise', related_name='training_programs')

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()

    def __str__(self):
        return self.name
