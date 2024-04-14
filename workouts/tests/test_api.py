from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from workouts.models import Exercise
from workouts.serializers import ExerciseSerializer


class ExerciseApiTestCase(APITestCase):
    def setUp(self):
        self.exercises_1 = Exercise.objects.create(name='Exercises_1', description='Спина')
        self.exercises_2 = Exercise.objects.create(name='Exercises_2', description='Ноги')
        self.exercises_3 = Exercise.objects.create(name='Exercises_3 Спина', description='Руки и Спина')

    def test_get(self):
        url = reverse('exercise-list')
        response = self.client.get(url)
        serializer_data = ExerciseSerializer([self.exercises_1, self.exercises_2, self.exercises_3], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('exercise-list')
        response = self.client.get(url,data={'search': 'Спина'})
        serializer_data = ExerciseSerializer([self.exercises_1, self.exercises_3], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)
