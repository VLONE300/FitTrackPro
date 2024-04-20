from django.urls import path
from rest_framework.routers import SimpleRouter

from workouts.views import ExerciseViewSet, TrainingExerciseViewSet, TrainingProgramViewSet, MyProgramViewSet, \
    ExerciseResultViewSet

router = SimpleRouter()
router.register(r'exercise', ExerciseViewSet)
router.register(r'training-exercise', TrainingExerciseViewSet)
router.register(r'programs', TrainingProgramViewSet)
router.register(r'my-programs', MyProgramViewSet, basename='my-programs')
router.register(r'exercise-result', ExerciseResultViewSet, basename='exercise-result')

urlpatterns = [
]

urlpatterns += router.urls
