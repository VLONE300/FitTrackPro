from django.contrib import admin
from workouts.models import TrainingProgram, Exercise, ExerciseResult

admin.site.register(TrainingProgram)
admin.site.register(Exercise)
admin.site.register(ExerciseResult)
