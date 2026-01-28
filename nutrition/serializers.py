from rest_framework import serializers
from nutrition.models import CookingTime, Ingredient, Nutrition, PhotoAI


class CookingTimeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CookingTime
        fields = ('id', 'duration_minutes', 'user')

class IngredientSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'user')

class NutritionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Nutrition
        fields = '__all__'

class PhotoAISerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoAI
        fields = ('id', 'image', 'ai_result', 'created_at', )
        read_only_fields = ('id', 'ai_result', 'created_at', )

    def validate_image(self, image):
        if image.size > 5 * 1024 * 1024:
            raise serializers.ValidationError("Максимум 5MB")
        return image