from rest_framework import serializers

from users.models import Trainer, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number',)


class TrainerSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Trainer
        fields = ('user', 'contacts', 'work_experience')
