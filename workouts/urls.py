from django.urls import path
from rest_framework.routers import SimpleRouter

from workouts.views import ExerciseViewSet, TrainingExerciseViewSet,TrainingProgramViewSet

router = SimpleRouter()
router.register(r'exercise', ExerciseViewSet)
router.register(r'training-exercise', TrainingExerciseViewSet)
router.register(r'programs', TrainingProgramViewSet)

urlpatterns = [
]

urlpatterns += router.urls
