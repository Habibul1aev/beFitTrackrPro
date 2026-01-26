from rest_framework import routers
from nutrition import views

router = routers.DefaultRouter()
router.register('nutrition', views.NutritionViewSet)
router.register('cookingtime', views.CookingViewSet)
router.register('ingredient', views.IngredientViewSet)


urlpatterns = router.urls
