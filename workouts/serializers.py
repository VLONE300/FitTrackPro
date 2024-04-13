from rest_framework import serializers

from workouts.models import TrainingProgram, TrainingExercise, Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


# class TrainingExerciseSerializer(serializers.ModelSerializer):
#     exercise = serializers.StringRelatedField()
#
#     class Meta:
#         model = TrainingExercise
#         fields = ('exercise', 'sets', 'reps')
#
#
# class TrainingProgramSerializer(serializers.ModelSerializer):
#     exercises = TrainingExercise(many=True, read_only=True)
#
#     class Meta:
#         model = TrainingProgram
#         fields = ('id', 'name', 'description', 'exercises')
