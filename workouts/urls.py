from django.urls import path
from rest_framework.routers import SimpleRouter

from workouts.views import ExerciseViewSet

router = SimpleRouter()
router.register(r'exercise', ExerciseViewSet)

urlpatterns = [
    # path('training-programs/', TrainingProgramslistView.as_view(), name='training_programs_list'),
]

urlpatterns += router.urls
