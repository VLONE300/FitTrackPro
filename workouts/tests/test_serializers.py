from django.test import TestCase

from workouts.models import Exercise
from workouts.serializers import ExerciseSerializer


class ExerciseSerializerTestCase(TestCase):
    def test_ok(self):
        exercises_1 = Exercise.objects.create(name='Exercises_1', description='-')
        exercises_2 = Exercise.objects.create(name='Exercises_2', description='-')
        data = ExerciseSerializer([exercises_1, exercises_2], many=True).data
        expected_data = [
            {
                'id': exercises_1.id,
                'name': "Exercises_1",
                'description': "-",
            },
            {
                'id': exercises_2.id,
                'name': "Exercises_2",
                'description': "-",
            }
        ]
        self.assertEqual(expected_data, data)
