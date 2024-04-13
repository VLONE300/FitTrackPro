from rest_framework import serializers

from workouts.models import TrainingProgram, TrainingExercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingExercise
        fields = ('exercise', 'sets', 'reps')


class TrainingProgramSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = TrainingProgram
        fields = ('name', 'description', 'exercises')
