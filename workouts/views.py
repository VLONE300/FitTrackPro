from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from workouts.models import TrainingProgram
from workouts.serializers import TrainingProgramSerializer


class TrainingProgramslistView(ListAPIView):
    queryset = TrainingProgram.objects.filter(training_type='General ')
    serializer_class = TrainingProgramSerializer
    permission_classes = [AllowAny]
