from django.contrib import admin
from workouts.models import TrainingProgram, Exercise, ExerciseResult, TrainingExercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(TrainingExercise)
class TrainingExerciseAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'sets', 'reps')


admin.site.register(TrainingProgram)
admin.site.register(ExerciseResult)
