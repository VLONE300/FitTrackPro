from django.urls import path

from workouts.views import TrainingProgramslistView

urlpatterns = [
    path('', TrainingProgramslistView.as_view(), name='training_programs_list')
]