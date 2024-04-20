from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

from workouts.models import Exercise, TrainingExercise, TrainingProgram, ExerciseResult
from workouts.serializers import ExerciseSerializer, TrainingExerciseSerializer, TrainingProgramSerializer, \
    MyProgramSerializer, ExerciseResultSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']


class TrainingExerciseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = TrainingExercise.objects.all()
    serializer_class = TrainingExerciseSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['sets']
    ordering_fields = ['sets']


class TrainingProgramViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = TrainingProgram.objects.filter(training_type='General')
    serializer_class = TrainingProgramSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MyProgramViewSet(viewsets.ModelViewSet):
    serializer_class = MyProgramSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = TrainingProgram.objects.filter(user=self.request.user)
        return queryset


class ExerciseResultViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = ExerciseResult.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
