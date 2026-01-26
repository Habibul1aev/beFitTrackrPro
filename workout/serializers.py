from rest_framework import serializers
from workout.models import Workout, Exercise


class WorkoutSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Workout
        fields = '__all__'


class ExerciseSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Exercise
        fields = '__all__'