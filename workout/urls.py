from workout import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('workout', views.WorkoutViewSet)
router.register('exercise', views.ExerciseViewSet)


urlpatterns = router.urls