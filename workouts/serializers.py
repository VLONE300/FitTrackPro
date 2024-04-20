from rest_framework import serializers

from workouts.models import Exercise, TrainingExercise, TrainingProgram


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'name', 'description')


class TrainingExerciseSerializer(serializers.ModelSerializer):
    exercise = serializers.PrimaryKeyRelatedField(queryset=Exercise.objects.all())

    class Meta:
        model = TrainingExercise
        fields = ('id', 'exercise', 'sets', 'reps')


class TrainingProgramSerializer(serializers.ModelSerializer):
    exercises = TrainingExerciseSerializer(many=True)

    class Meta:
        model = TrainingProgram
        fields = ('id', 'name', 'description', 'training_type', 'exercises')

    def create(self, validated_data):
        exercises_data = validated_data.pop('exercises')
        training_program = TrainingProgram.objects.create(**validated_data)
        for exercise_data in exercises_data:
            exercise = TrainingExercise.objects.create(**exercise_data)
            training_program.exercises.add(exercise)
        return training_program
