from django.contrib import admin
from workouts.models import TrainingProgram, Exercise, ExerciseResult, TrainingExercise

admin.site.register(TrainingProgram)
admin.site.register(Exercise)
admin.site.register(ExerciseResult)
admin.site.register(TrainingExercise)
