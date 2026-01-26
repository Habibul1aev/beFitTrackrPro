from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Fitness API",
        default_version='v1',
        description="API для мобильного приложения",
        contact=openapi.Contact(email="support@example.com"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),  # login logout

    path('api/v1/auth/', include('djoser.urls')),  # users, set_password, me,
    path('api/v1/auth/', include('djoser.urls.authtoken')),  # drf token

    path('api/v1/workouts/', include('workout.urls')),
    path('api/v1/nutritions/', include('nutrition.urls')),
    path('api/v1/accounts/', include('account.urls')),

    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
