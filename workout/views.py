from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.shortcuts import render

from workout.models import Workout, Exercise
from workout.pagination import WorkoutPagination
from workout.permissions import IsAdminOrReadOnly
from workout.serializers import WorkoutSerializer, ExerciseSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = (IsAdminOrReadOnly, )
    pagination_class = WorkoutPagination

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = (IsAdminOrReadOnly, )



