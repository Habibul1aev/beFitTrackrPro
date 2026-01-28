from rest_framework import generics, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from nutrition.models import CookingTime, Ingredient, Nutrition, PhotoAI
from nutrition.serializers import CookingTimeSerializer, IngredientSerializer, NutritionSerializer, PhotoAISerializer
from nutrition.permissions import IsAdminOrReadOnly
from nutrition.utils import analysis_photo


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
    serializer_class = PhotoAISerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    http_method_names = ['get', 'post', 'delete']

    def get_queryset(self):
        return PhotoAI.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        photo = serializer.save(user=request.user)

        ai_result = analysis_photo(photo.image.path)

        photo.ai_result = ai_result
        photo.save(update_fields=["ai_result"])

        return Response(
            {
                "id": photo.id,
                "result": ai_result
            },
            status=201
        )



