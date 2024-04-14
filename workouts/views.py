from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated

from workouts.models import Exercise, TrainingExercise, TrainingProgram
from workouts.serializers import ExerciseSerializer, TrainingExerciseSerializer, TrainingProgramSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']


class TrainingExerciseViewSet(viewsets.ModelViewSet):
    queryset = TrainingExercise.objects.all()
    serializer_class = TrainingExerciseSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['sets']
    ordering_fields = ['sets']


class TrainingProgramViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TrainingProgram.objects.filter(training_type='General ')
    serializer_class = TrainingProgramSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
