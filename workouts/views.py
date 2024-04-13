from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from workouts.models import TrainingProgram, Exercise
from workouts.serializers import ExerciseSerializer


class ExerciseViewSet(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


# class TrainingProgramslistView(ListAPIView):
#     queryset = TrainingProgram.objects.filter(training_type='General ')
#     serializer_class = TrainingProgramSerializer
#     permission_classes = [AllowAny]
