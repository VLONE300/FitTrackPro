from rest_framework import serializers

from trainers.models import UserTrainingProgram, UserProgress
from users.models import Trainer, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number',)


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ('first_name', 'last_name', 'contacts', 'work_experience')


class TrainersProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTrainingProgram
        fields = ['id', 'trainer', 'user', 'program', 'start_date', 'end_date']
        read_only_fields = ['trainer']


class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = ['id', 'user_program', 'date', 'weight']
