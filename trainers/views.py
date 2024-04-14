from requests import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from trainers.models import UserTrainingProgram
from trainers.permissions import IsTrainer, IsTrainerOfTrainingProgram
from trainers.serializers import TrainerSerializer, TrainersProgramSerializer
from users.models import Trainer, CustomUser


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
        trainer = Trainer.objects.get(user=user)
        serializer.save(trainer=trainer)

    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            permissions_classes = [IsAuthenticated, IsTrainerOfTrainingProgram]
        else:
            permissions_classes = [IsAuthenticated, IsTrainer]
        return [permission() for permission in permissions_classes]
