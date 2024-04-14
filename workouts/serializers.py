from rest_framework import serializers

from workouts.models import Exercise, TrainingExercise, TrainingProgram


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'name', 'description')


class TrainingExerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(read_only=True)

    class Meta:
        model = TrainingExercise
        fields = ('id', 'exercise', 'sets', 'reps')


class TrainingProgramSerializer(serializers.ModelSerializer):
    exercises = TrainingExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = TrainingProgram
        fields = ('id', 'name', 'description', 'training_type', 'exercises')
