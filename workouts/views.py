from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from workouts.models import Exercise, TrainingExercise, TrainingProgram, ExerciseResult
from workouts.serializers import ExerciseSerializer, TrainingExerciseSerializer, TrainingProgramSerializer, \
    MyProgramSerializer, ExerciseResultSerializer
from workouts.tasks import send_create_program_mail


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
    filter_backends = [OrderingFilter]
    filterset_fields = ['sets']
    ordering_fields = ['sets']


class TrainingProgramViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = TrainingProgram.objects.filter(training_type='General')
    serializer_class = TrainingProgramSerializer



class MyProgramViewSet(viewsets.ModelViewSet):
    serializer_class = MyProgramSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = TrainingProgram.objects.filter(user=self.request.user)
        print(hasattr(self.request.user, 'trainer'))
        return queryset


class ExerciseResultViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = ExerciseResult.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
