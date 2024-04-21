from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from trainers.models import UserTrainingProgram, UserProgress
from trainers.permissions import IsTrainer, IsTrainerOfTrainingProgram
from trainers.serializers import TrainerSerializer, TrainersProgramSerializer, UserProgressSerializer
from users.models import Trainer


class TrainersListView(ListAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    permission_classes = [AllowAny]


class TrainersProgramView(ModelViewSet):
    queryset = UserTrainingProgram.objects.all()
    serializer_class = TrainersProgramSerializer
    permission_classes = [IsAuthenticated, IsTrainer]

    def perform_create(self, serializer):
        user = self.request.user
        trainer = Trainer.objects.get(email=user.email)
        serializer.save(trainer=trainer)

    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            permissions_classes = [IsAuthenticated, IsTrainerOfTrainingProgram]
        else:
            permissions_classes = [IsAuthenticated, IsTrainer]
        return [permission() for permission in permissions_classes]


class UserProgressView(ModelViewSet):
    queryset = UserProgress.objects.all()
    serializer_class = UserProgressSerializer
    permission_classes = [IsTrainer]
