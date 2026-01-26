from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from nutrition.models import CookingTime, Ingredient, Nutrition, PhotoAI
from nutrition.serializers import CookingTimeSerializer, IngredientSerializer, NutritionSerializer, PhotoAISerializer
from nutrition.permissions import IsAdminOrReadOnly

class CookingViewSet(viewsets.ModelViewSet):
    queryset = CookingTime.objects.all()
    serializer_class = CookingTimeSerializer
    permissions_classes = (IsAdminOrReadOnly,)

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permissions_classes = (IsAdminOrReadOnly, )


class NutritionViewSet(viewsets.ModelViewSet):
    queryset = Nutrition.objects.all()
    serializer_class = NutritionSerializer
    permissions_classes = (IsAdminOrReadOnly,)

class PhotoAIViewsSet(viewsets.ModelViewSet):
    queryset = PhotoAI.objects.all()
    serializer_class = PhotoAISerializer
